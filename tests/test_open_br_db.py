import pytest
from jsonschema import validate
import random


@pytest.mark.parametrize('city', ['New York', 'Los Angeles', 'Boston'])
def test_get_brewery_by_city(breweries_api_client, city):
    result = breweries_api_client.get(
        path='?by_city=' + city
    ).json()
    for i in range(0, len(result)):
        assert result[i]['city'] == city


@pytest.mark.parametrize('per_page', [15, 30, 50])
def test_breweries_per_page(breweries_api_client, per_page):
    result = breweries_api_client.get(
        path='?per_page=' + str(per_page)
    ).json()
    assert len(result) == per_page


def test_brewery_json_schema(breweries_api_client):
    random_brewery_id = random.randint(1, 8029)
    result = breweries_api_client.get(
        path='/' + str(random_brewery_id)
    )

    schema = {
        "id": "number",
        "name": "string",
        "brewery_type": "string",
        "street": "string",
        "city": "string",
        "state": "string",
        "postal_code": "string",
        "country": "string",
        "longitude": "string",
        "latitude": "string",
        "phone": "string",
        "website_url": "string",
        "updated_at": "string",
        "tag_list": "array"
    }

    validate(instance=result.json(), schema=schema)


def test_get_brewery(breweries_api_client):
    random_brewery_id = random.randint(1, 8029)
    result = breweries_api_client.get(
        path='/' + str(random_brewery_id)
    )
    assert result.json()['id'] == random_brewery_id


@pytest.mark.parametrize('word', ['fox', 'brew', 'blue'])
def test_autocomplete(breweries_api_client, word):
    result = breweries_api_client.get(
        path='/autocomplete?query=' + word
    ).json()
    assert word in result[0]['name'].lower()
