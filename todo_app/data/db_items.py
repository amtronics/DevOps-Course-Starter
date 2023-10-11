import typing
import pymongo
import os
import pprint


class Item:
    TODO = "To Do"
    DONE = "Done"
    ''' Class to represent an item'''
    def __init__(self, name: str, status=None):
        if not status:
            status = Item.TODO
        self.name = name
        self.status = status

        return self._get_item()
    
    def _get_item(self):
        item = {
            "name": self.name,
            "status": self.status
        }
        return item


class TrelloAPI():
    ''' Service Trello API related actions '''
    def __init__(self) -> None:
        CONNECTION_STRING = os.environ.get('CONNECTION_STRING')
        DATABSE_NAME = os.environ.get('DATABSE_NAME')

        client = pymongo.MongoClient(CONNECTION_STRING)
        self.database = client[DATABSE_NAME]
        self.collection = self.database['todo_items']
        self.items = self.collection.find()
        pprint.pprint(self.items)

    # def _send_request(self, url, method='GET', **query):
    #     '''
    #     Send a request to Trello API

    #     Args:
    #         url: url after https://api.trello.com/1/
    #         query: kwargs for HTML query, excluding API Key & Token

    #     Returns:
    #         JSON response
    #     '''
    #     url = f"https://api.trello.com/1/{url}"
    #     headers = {"Accept": "application/json"}
    #     _query = {"key": self.API_KEY,
    #               "token": self.API_TOKEN}
    #     _query.update(query)
    #     response = requests.request(method=method, url=url, headers=headers, params=_query, verify=False)
    #     return response.json()
    # def save_item(self, id, new_status):
    #     """
    #     Updates an existing item in the Trello. If no existing item matches the ID of the specified item, nothing is saved.

    #     Args:
    #         id: The id of item to change
    #         new_status: new status of the item
    #     """
    #     lst_id = [lst.id for lst in self.lists if lst.name == new_status][0]
    #     url = f"cards/{id}"
    #     query = {"idList": lst_id}
    #     self._send_request(url, 'PUT', **query)

    def add_item(self, name: str):
        """
        Adds a new item with the specified name to the Database.

        Args:
            name: The name of the item.
        """
        self.collection.insert_one(Item(name))
