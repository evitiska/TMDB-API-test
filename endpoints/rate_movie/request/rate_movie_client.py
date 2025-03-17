import requests
from utils.base_api_client import TMDBAPIClient

class RateMovieTMDBAPIClient(TMDBAPIClient):    
    def rate(self, movie_id, rating, guest_session_id):
        response = requests.post(
            f"{self.base_url}/movie/{movie_id}/rating",
            params={
                "api_key": self.api_key,
                "guest_session_id": guest_session_id,
            },
            json={"value": rating},
        )
        return response