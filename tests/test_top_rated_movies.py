import pytest
from endpoints.top_rated_movies.client.top_rated_movies_client import TopRatedMoviesClient 
from endpoints.top_rated_movies.schema.top_rated_movies_schema import TOP_RATED_MOVIES_RESPONSE_SCHEMA
from jsonschema import validate

client = TopRatedMoviesClient()

def test_top_rated_movies_OK():
    response = client.get()
    assert response.status_code == 200

    json_data = response.json()
    validate(json_data, TOP_RATED_MOVIES_RESPONSE_SCHEMA)

def test_top_rated_movies_pagination():
    response = client.get(page=5)
    assert response.status_code == 200

    json_data = response.json()
    validate(json_data, TOP_RATED_MOVIES_RESPONSE_SCHEMA)
    assert json_data["page"] == 5

def test_top_rated_movies_invalid_pagination():
    response = client.get(page=-1)  
    assert response.status_code == 400 
    
def test_top_rated_movies_invalid_pagination2():
    response = client.get(page=999999999)  
    assert response.status_code == 400

def test_top_rated_movies_language():
    response = client.get(language="fr-FR")  
    assert response.status_code == 200 

    json_data = response.json()
    validate(json_data, TOP_RATED_MOVIES_RESPONSE_SCHEMA)

def test_top_rated_movies_invalid_api_key():
    client = TopRatedMoviesClient(api_key="bogus_api_key")
    response = client.get()
    assert response.status_code == 401

def test_top_rated_movies_missing_api_key():
    client = TopRatedMoviesClient()
    response = client.get(include_api_key=False)
    assert response.status_code == 401
