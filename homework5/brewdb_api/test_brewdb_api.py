"""
descriptions to modules for testing api https://www.openbrewerydb.org/
"""
import pytest
import requests
from jsonschema import validate


def test_api_status_code(base_url):
    """method for test correct page status code"""

    response = requests.get(base_url, timeout=5)
    assert response.status_code == 200


def test_schema_brewereis(base_url):
    """method to check valid schema response """

    response = requests.get(f"{base_url}/breweries", timeout=5)
    assert response.status_code == 200
    resp = response.json()
    schema = {
        "type": "array",
        "items": {
            "type": "object"
        }
    }
    validate(resp, schema)


@pytest.mark.parametrize("id", ["b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0",
                                "faf0e458-0f8c-4ad0-990a-e803c574a1e2",
                                "6260eac2-6949-4c19-aec9-739c2cdcf849",
                                "68cb3ab3-3136-419e-aff6-06d965cfb280"],
                         ids=["MadTree", "River", "state 48",
                              "Special Brewing"])
def test_id_list(base_url, id):
    """method for test correct page status code and correct page id"""

    url = requests.get(f"{base_url}/breweries/{id}", timeout=5)
    assert url.status_code == 200
    response = url.json()
    assert response["id"] == id


def test_query_search(base_url):
    """method to check search status code"""

    response = requests.get(f"{base_url}"
                            f"/breweries/search?query=california",
                            timeout=5)
    assert response.status_code == 200


@pytest.mark.parametrize("size", [1, 3, 5])
def test_search_size(base_url, size):
    """method to check search status code and correct response json size"""

    response = requests.get(f"{base_url}/breweries/random?size={size}]",
                            timeout=5)
    if response.status_code == 200:
        data = response.json()
        assert len(data) == size
