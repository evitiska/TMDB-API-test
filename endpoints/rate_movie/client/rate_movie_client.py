import requests
from endpoints.base_api_client import APIBaseClient

class RateMovieClient(APIBaseClient):    
    def rate(self, movie_id, rating, guest_session_id, include_api_key = True):
        params = {"guest_session_id": guest_session_id}
        if include_api_key:
            params["api_key"] = self.api_key

        response = requests.post(
            f"{self.base_url}/movie/{movie_id}/rating",
            params=params,
            json={"value": rating},
        )
        return response