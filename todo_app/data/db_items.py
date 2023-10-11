import typing
import pymongo
import os
import pprint
from bson.objectid import ObjectId


class Item:
    TODO = "To Do"
    DONE = "Done"
    ''' Class to represent an item'''
    def __init__(self, name: str, status=None) -> dict:
        if not status:
            status = Item.TODO
        self.name = name
        self.status = status
    
    @property
    def obj(self) -> dict:
        item = {
            "name": self.name,
            "status": self.status
        }
        return item


class DatabaseAPI():
    ''' Service MongoDB API related actions '''
    def __init__(self) -> None:
        CONNECTION_STRING = os.environ.get('CONNECTION_STRING')
        DATABSE_NAME = os.environ.get('DATABSE_NAME')

        client = pymongo.MongoClient(CONNECTION_STRING)
        self.database = client[DATABSE_NAME]
        self.collection = self.database['todo_items']

    @property
    def items(self):
        items = self.collection.find()
        sorted_items = sorted(items, key=lambda x: x["name"].lower())
        return sorted_items

    def save_item(self, id: str, new_status: str):
        """
        Updates an existing item in the Database. If no existing item matches the ID of the specified item, nothing is saved.

        Args:
            id: The id of item to change
            new_status: new status of the item
        """
        _id = ObjectId(id)
        self.collection.update_one({'_id': _id}, {'$set': {'status': new_status}})



    def add_item(self, name: str):
        """
        Adds a new item with the specified name to the Database.

        Args:
            name: The name of the item.
        """
        item = Item(name)
        self.collection.insert_one(item.obj).inserted_id
