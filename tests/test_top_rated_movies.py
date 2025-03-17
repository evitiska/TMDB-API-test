import pytest
from endpoints.top_rated_movies.request import top_rated_movies_client
from endpoints.top_rated_movies.schema.top_rated_movies_response import TOP_RATED_MOVIES_RESPONSE_SCHEMA
from jsonschema import validate

def test_top_rated_movies_OK():
    client = top_rated_movies_client.TopRatedMoviesTMDBAPIClient()
    response = client.get()
    assert response.status_code == 200

    json_data = response.json()
    validate(json_data, TOP_RATED_MOVIES_RESPONSE_SCHEMA)

def test_top_rated_movies_pagination():
    client = top_rated_movies_client.TopRatedMoviesTMDBAPIClient()
    response = client.get(page=5)
    assert response.status_code == 200

    json_data = response.json()
    validate(json_data, TOP_RATED_MOVIES_RESPONSE_SCHEMA)
    assert json_data["page"] == 5

def test_top_rated_movies_invalid_api_key():
    client = top_rated_movies_client.TopRatedMoviesTMDBAPIClient(api_key="bogus_api_key")
    response = client.get()
    assert response.status_code == 401

def test_top_rated_movies_invalid_pagination():
    client = top_rated_movies_client.TopRatedMoviesTMDBAPIClient()
    response = client.get(page=-1)  
    assert response.status_code == 400  #401?
    
def test_top_rated_movies_invalid_pagination2():
    client = top_rated_movies_client.TopRatedMoviesTMDBAPIClient()
    response = client.get(page=999999999)  
    assert response.status_code == 400 #401?

def test_top_rated_movies_language():
    client = top_rated_movies_client.TopRatedMoviesTMDBAPIClient()
    response = client.get(language="fr-FR")  
    assert response.status_code == 200 

    json_data = response.json()
    validate(json_data, TOP_RATED_MOVIES_RESPONSE_SCHEMA)
