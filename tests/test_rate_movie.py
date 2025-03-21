import pytest
from jsonschema import validate
from utils.config import TEST_MOVIE_ID
from endpoints.rate_movie.client.rate_movie_client import RateMovieClient
from endpoints.guest_session.client.guest_session_client import GuestSessionClient
from endpoints.guest_session.schema.new_guest_session_schema import NEW_GUEST_SESSION_RESPONSE_SCHEMA
from endpoints.rate_movie.schema.rate_movie_schema import RATED_MOVIE_RESPONSE_SCHEMA

@pytest.fixture(scope='module')
def guest_session():
    client = GuestSessionClient()
    response = client.create_new_session()
    assert response.status_code == 200
    json_data = response.json()
    validate(json_data, NEW_GUEST_SESSION_RESPONSE_SCHEMA)
    guest_session_id = json_data["guest_session_id"]
    assert guest_session_id is not None
    return guest_session_id

client = RateMovieClient()

def test_rate_movie_session_id_missing():
    response = client.rate(movie_id=TEST_MOVIE_ID, rating=10, guest_session_id=None)
    assert response.status_code == 401
    validate(response.json(), RATED_MOVIE_RESPONSE_SCHEMA)

def test_rate_movie_session_id_invalid():
    response = client.rate(movie_id=TEST_MOVIE_ID, rating=10, guest_session_id="bogus_session_id")
    assert response.status_code == 401
    validate(response.json(), RATED_MOVIE_RESPONSE_SCHEMA)

def test_rate_movie_api_key_invalid():
    client = RateMovieClient(api_key="bogus_api_key")
    response = client.rate(movie_id=TEST_MOVIE_ID, rating=10, guest_session_id=None)
    assert response.status_code == 401
    validate(response.json(), RATED_MOVIE_RESPONSE_SCHEMA)

def test_rate_movie_api_key_missing():
    client = RateMovieClient()
    response = client.rate(movie_id=TEST_MOVIE_ID, rating=10, guest_session_id=None, include_api_key=False)
    assert response.status_code == 401
    validate(response.json(), RATED_MOVIE_RESPONSE_SCHEMA)

def test_rate_movie_valid_rating(guest_session):
    response = client.rate(movie_id=TEST_MOVIE_ID, rating=10, guest_session_id=guest_session)
    assert response.status_code == 201
    validate(response.json(), RATED_MOVIE_RESPONSE_SCHEMA)

def test_rate_movie_rating_too_high(guest_session):
    response = client.rate(movie_id=TEST_MOVIE_ID, rating=999, guest_session_id=guest_session)
    assert response.status_code == 400
    validate(response.json(), RATED_MOVIE_RESPONSE_SCHEMA)

def test_rate_movie_rating_too_low(guest_session):
    response = client.rate(movie_id=TEST_MOVIE_ID, rating=-20, guest_session_id=guest_session)
    assert response.status_code == 400
    validate(response.json(), RATED_MOVIE_RESPONSE_SCHEMA)
    