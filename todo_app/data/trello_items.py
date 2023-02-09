from functools import cached_property
from urllib3.exceptions import InsecureRequestWarning
import typing
import requests
import os


# Suppress the warnings from urllib3
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


class Item:
    ''' Class to represent an item (card)'''
    def __init__(self, id, name, status='To Do'):
        self.id = id
        self.name = name
        self.status = status

    @classmethod
    def from_trello_card(cls, card, list):
        return cls(card['id'], card['name'], list['name'])


class TrelloList:
    ''' Class to represent a List'''
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @classmethod
    def from_trello_list(cls, list):
        return cls(list['id'], list['name'])


class TrelloAPI():
    ''' Service Trello API related actions '''
    def __init__(self) -> None:
        self.API_KEY = os.environ.get('API_KEY')
        self.API_TOKEN = os.environ.get('API_TOKEN')
        self.BOARD_ID = os.environ.get('BOARD_ID')
        self.cards : typing.List[Item] = []
        self.lists : typing.List[TrelloList] = []

        # call get_items to initialise in RAM cards and lists properties
        self.get_items()

    def _send_request(self, url, method='GET', **query):
        '''
        Send a request to Trello API

        Args:
            url: url after https://api.trello.com/1/
            query: kwargs for HTML query, excluding API Key & Token

        Returns:
            JSON response
        '''
        url = f"https://api.trello.com/1/{url}"
        headers = {"Accept": "application/json"}
        _query = {"key": self.API_KEY,
                  "token": self.API_TOKEN}
        _query.update(query)
        response = requests.request(method, url, headers=headers, params=_query, verify=False)
        return response.json()

    def get_items(self):
        """
        Fetches all saved items from Trello.

        Returns:
            list: The list of saved items.
        """
        self.cards = []
        self.lists = []
        url = f"boards/{self.BOARD_ID}/lists"
        query = {"cards": "open", "card_fields": "id,name,idList"}
        for trello_list in self._send_request(url, **query):
            for card in trello_list['cards']:
                self.cards.append(Item.from_trello_card(card, trello_list))
            self.lists.append(TrelloList.from_trello_list(trello_list))
        return self.cards

    def save_item(self, id, new_status):
        """
        Updates an existing item in the Trello. If no existing item matches the ID of the specified item, nothing is saved.

        Args:
            id: The id of item to change
            new_status: new status of the item
        """
        lst_id = [lst.id for lst in self.lists if lst.name == new_status][0]
        url = f"cards/{id}"
        query = {"idList": lst_id}
        self._send_request(url, 'PUT', **query)

    def add_item(self, name):
        """
        Adds a new item with the specified name to the Trello.

        Args:
            name: The name of the item.
        """
        lst_id = [lst.id for lst in self.lists if lst.name == "To Do"][0]
        query = {"idList": lst_id, "name": name}
        self._send_request("cards/", 'POST', **query)
