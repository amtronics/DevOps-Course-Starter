from todo_app.data.db_items import Item


class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def done_items(self):
        return [it for it in self.items if it["status"] == Item.DONE]

    @property
    def todo_items(self):
        return [it for it in self.items if it["status"] == Item.TODO]
