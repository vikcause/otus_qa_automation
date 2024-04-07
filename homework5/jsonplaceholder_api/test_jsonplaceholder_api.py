"""
Methods for testing https://jsonplaceholde.typicode.com/
"""
import pytest

POST_MAX = 100
PHOTOS_MAX = 5000


@pytest.mark.parametrize("post_id", [1, POST_MAX])
def test_check_id(base_url, session, post_id):
    """method to check status code and post id"""

    response = session.get(f"{base_url}/posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["id"] == post_id


@pytest.mark.parametrize("post_id", [-1, 0, "sometext", POST_MAX + 1])
def test_negative_check(base_url, session, post_id):
    """negative checking for session"""

    resp = session.get(f"{base_url}/posts/{post_id}")
    assert resp.status_code == 404
    assert resp.json() == {}


def test_check_post_length(base_url, session):
    """method to check all post count"""

    res = session.get(f"{base_url}/posts")
    assert len(res.json()) == POST_MAX


def test_photos_length(base_url, session):
    """method to check all photos count"""

    resp_check = session.get(f"{base_url}/photos")
    assert resp_check.status_code == 200
    assert len(resp_check.json()) == PHOTOS_MAX


def test_create(session, base_url):
    """method to create some user"""

    payload = {"title": "newUser", "body": "text-to-text", "userId": 7}
    response = session.post(f"{base_url}/posts", json=payload)

    assert response.status_code == 201
    json_resp = response.json()
    assert json_resp["id"] == POST_MAX + 1
    assert json_resp["userId"] == payload["userId"]
    assert json_resp["title"] == payload["title"]
    assert json_resp["body"] == payload["body"]


@pytest.mark.parametrize("id", [1, 7, 15], ids=["id - 1", "id - 7", "id - 15"])
def test_delete(session, base_url, id):
    """method to delete user by id"""

    response = session.delete(f"{base_url}/posts/{id}")
    assert response.status_code == 200
    assert len(response.json()) == 0
