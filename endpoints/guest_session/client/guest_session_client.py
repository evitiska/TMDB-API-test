import requests
from endpoints.base_api_client import APIBaseClient

class GuestSessionClient(APIBaseClient):
    def create_new_session(self):
        response = requests.get(
            f"{self.base_url}/authentication/guest_session/new",
            params={"api_key": self.api_key},
        )
        return response