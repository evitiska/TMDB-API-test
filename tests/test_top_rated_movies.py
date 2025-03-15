import pytest
from utils import api_client 
from utils.models.top_rated_movies_response import TOP_RATED_MOVIES_RESPONSE_SCHEMA
from jsonschema import validate

def test_top_rated_movies_OK():
    client = api_client.TMDBClient()
    response = client.get_top_rated_movies()
    assert response.status_code == 200

    json_data = response.json()
    validate(json_data, TOP_RATED_MOVIES_RESPONSE_SCHEMA)

def test_top_rated_movies_pagination():
    client = api_client.TMDBClient()
    response = client.get_top_rated_movies(page=5)
    assert response.status_code == 200

    json_data = response.json()
    validate(json_data, TOP_RATED_MOVIES_RESPONSE_SCHEMA)
    assert json_data["page"] == 5

def test_top_rated_movies_invalid_api_key():
    client = api_client.TMDBClient(api_key="bogus_api_key")
    response = client.get_top_rated_movies()
    assert response.status_code == 401
    