from functools import cached_property
import requests
import json
import os


class TrelloItems():
    ''' Service Trello API related actions '''
    def __init__(self) -> None:
        self.API_KEY = os.environ.get('API_KEY')
        self.API_TOKEN = os.environ.get('API_TOKEN')
        self.BOARD_ID = os.environ.get('BOARD_ID')

    def _request_lists(self):
        ''' Get Filtered Lists on a Board '''
        url = f"https://api.trello.com/1/boards/{self.BOARD_ID}/lists"
        headers = {"Accept": "application/json"}
        query = {"key": self.API_KEY,
                 "token": self.API_TOKEN,
                 "cards": "open",
                 "card_fields": "id,name,idList"}
        response = requests.request("GET", url, headers=headers, params=query, verify=False)
        return response.json()

    @cached_property
    def _status_idlist_mapping(self):
        mapping = {}
        for trello_list in self._request_lists():
            mapping[trello_list['id']] = trello_list['name']
        return mapping

    def get_items(self):
        """
        Fetches all saved items from the Trello.

        Returns:
            list: The list of saved items.
        """
        cards = []
        for trello_list in self._request_lists():
            for card in trello_list['cards']:
                cards.append({'id': card['id'],
                              'status': self._status_idlist_mapping[card['idList']],
                              'title': card['name']})
        return cards

    def get_item(self, id):
        """
        Fetches the saved item with the specified ID.

        Args:
            id: The ID of the item.

        Returns:
            item: The saved item, or None if no items match the specified ID.
        """
        items = self.get_items()
        return next((item for item in items if item['id'] == int(id)), None)

    # def add_item(self, title):
    #     """
    #     Adds a new item with the specified title to the Trello.

    #     Args:
    #         title: The title of the item.

    #     Returns:
    #         item: The saved item.
    #     """
    #     items = self.get_items()

    #     # Determine the ID for the item based on that of the previously added item
    #     id = items[-1]['id'] + 1 if items else 0

    #     item = { 'id': id, 'title': title, 'status': 'Not Started' }

    #     # Add the item to the list
    #     items.append(item)
    #     # session['items'] = items

    #     return item

    # def save_item(self, item):
    #     """
    #     Updates an existing item in the Trello. If no existing item matches the ID of the specified item, nothing is saved.

    #     Args:
    #         item: The item to save.
    #     """
    #     existing_items = self.get_items()
    #     updated_items = [item if item['id'] == existing_item['id'] else existing_item for existing_item in existing_items]

    #     # session['items'] = updated_items

    #     return item