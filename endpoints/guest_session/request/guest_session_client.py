import requests
from utils.base_api_client import TMDBAPIClient

class GuestSessionTMDBAPIClient(TMDBAPIClient):
    def create_new_session(self):
        response = requests.get(
            f"{self.base_url}/authentication/guest_session/new",
            params={"api_key": self.api_key},
        )
        return response