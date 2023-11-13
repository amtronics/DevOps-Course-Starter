import os
import pytest
from todo_app import app
from dotenv import load_dotenv, find_dotenv
import mongomock

class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data


@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    with mongomock.patch(servers=(('fakemongo.com', 27017),)):
        test_app = app.create_app()
        with test_app.test_client() as client:
            yield client


def test_index(client):
    # Make a request to our app's index page
    response = client.get('/')

    assert response.status_code == 200


def test_complete_item(client):
    # Make a request to our app's complete_item endpoint
    response = client.post('/complete_item/6526bd5dedb8d7c9184cbaf4/Done')
    assert response.status_code == 302


def test_add_item(client):
    # Make a request to our app's add_item endpoint
    response = client.post('/add_item')
    assert response.status_code == 302
