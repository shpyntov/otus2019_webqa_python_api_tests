import pytest
from jsonschema import validate


@pytest.mark.parametrize('post_id', [10, 25, 50])
def test_get_post(jsonph_api_client, post_id):
    result = jsonph_api_client.get(
        path='/posts/' + str(post_id)
    )
    assert result.json()['id'] == post_id


@pytest.mark.parametrize('userid', [1, 10, 25])
def test_user_posts(jsonph_api_client, userid):
    result = jsonph_api_client.get(
        path='/posts?userId=' + str(userid)
    )
    for i in range(len(result.json())):
        assert result.json()[i]['userId'] == userid


@pytest.mark.parametrize('postid', [1, 10, 25])
def test_post_comments(jsonph_api_client, postid):
    result = jsonph_api_client.get(
        path='/comments?postId=' + str(postid)
    )
    for i in range(len(result.json())):
        assert result.json()[i]['postId'] == postid


def test_posts(jsonph_api_client):
    result = jsonph_api_client.get(
        path='/posts'
    )

    schema = {
        "userId": "number",
        "id": "number",
        "title": "string",
        "body": "string",
    }
    for i in range(len(result.json())):
        validate(instance=result.json()[i], schema=schema)

@pytest.mark.parametrize('userid', [1, 5, 10])
def test_user_id(jsonph_api_client, userid):
    result = jsonph_api_client.get(
        path='/users/' + str(userid)
    )
    assert result.json()['id'] == userid
