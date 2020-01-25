import pytest
import requests
import random


class APIClient:
    def __init__(self, base_address):
        self.base_address = base_address

    def post(self, path="/", params=None, data=None, headers=None):
        url = self.base_address + path
        return requests.post(url=url, params=params, data=data, headers=headers)

    def get(self, path="/", params=None):
        url = self.base_address + path
        return requests.get(url=url, params=params)


@pytest.fixture()
def dog_api_client():
    base_url = 'https://dog.ceo/api'
    return APIClient(base_url)


@pytest.fixture()
def random_breed(dog_api_client):
    breeds = dog_api_client.get(path='/breeds/list/all').json()['message']
    return random.choice(list(breeds))


@pytest.fixture()
def breweries_api_client():
    base_url = 'https://api.openbrewerydb.org/breweries'
    return APIClient(base_url)
