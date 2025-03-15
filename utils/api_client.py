import requests
from utils.config import BASE_URL, API_KEY

class TMDBClient:
    def __init__(self, api_key=None):
        self.api_key = api_key or API_KEY  # Use the passed API key or fallback to the default from config

    def get_top_rated_movies(self, page = None):
        params = {"api_key": self.api_key}
        
        if page is not None: 
            params["page"] = page

        response = requests.get(
            f"{BASE_URL}/movie/top_rated", params=params
        )
        return response
    
    def create_new_guest_session(self):
        response = requests.get(
            f"{BASE_URL}/authentication/guest_session/new",
            params={"api_key": self.api_key},
        )
        return response
    
    def rate_movie(self, movie_id, rating, guest_session_id):
        response = requests.post(
            f"{BASE_URL}/movie/{movie_id}/rating",
            params={
                "api_key": self.api_key,
                "guest_session_id": guest_session_id,
            },
            json={"value": rating},
        )
        return response
