import pytest


def test_random_image(dog_api_client):
    result = dog_api_client.get(
        path='/breeds/image/random'
    )
    assert result.json()['message'][-3:] == 'jpg'


def test_random_breed_image(dog_api_client, random_breed):
    result = dog_api_client.get(
        path='/breed/' + random_breed + '/images/random'
    )
    assert result.json()['message'][-3:] == 'jpg'


@pytest.mark.parametrize('images_count', [3, 5, 7])
def test_couple_images_by_breed(dog_api_client, random_breed, images_count):
    result = dog_api_client.get(
        path='/breed/' + random_breed + '/images/random/' + str(images_count)
    )
    assert len(result.json()['message']) == images_count


@pytest.mark.parametrize('breed', ["hound", "poodle", "retriever"])
def test_subbreed_not_null(dog_api_client, breed):
    result = dog_api_client.get(
        path='/breed/' + breed + '/list'
    )
    assert len(result.json()['message']) != 0


@pytest.mark.parametrize('breed, subbreed', [("retriever", "golden"), ("spaniel", "cocker"), ("terrier", "fox")])
def test_random_subbredd_image(dog_api_client, breed, subbreed):
    result = dog_api_client.get(
        path='/breed/' + breed + '/' + subbreed + '/images/random'
    )
    assert result.json()['message'][-3:] == 'jpg'
