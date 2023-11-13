from todo_app.data.view_model import ViewModel
from todo_app.data.db_items import Item
from random import choice
import typing
import pytest
import mongomock

@pytest.fixture
def random_items():
    
    items: typing.List[dict] = []
    for i in range(10):
        items.append(
            {"name": "item_number_{i}", "status": choice([Item.TODO, Item.DONE]), '_id': '6526bd5dedb8d7c9184cbaf4'}  # Random items with random statuses
            )

    return items


def test_view_model_done_items_property(random_items):
    # Arrange, handled by fixture
    # Act
    item_view_model = ViewModel(random_items)
    done_items = item_view_model.done_items

    # Assert
    for item in done_items:
        assert item in random_items, f"{item['name']} is not in the original items"

    for item in random_items:
        if item["status"] == Item.DONE:
            assert item in done_items, f"{item['name']} with status {item['status']} should have been returned"


def test_view_model_todo_items_property(random_items):
    # Arrange, handled by fixture
    # Act
    item_view_model = ViewModel(random_items)
    todo_items = item_view_model.todo_items

    # Assert
    for item in todo_items:
        assert item in random_items, f"{item['name']} is not in the original items"

    for item in random_items:
        if item['status'] == Item.TODO:
            assert item in todo_items, f"{item['name']} with status {item['status']} should have been returned"
