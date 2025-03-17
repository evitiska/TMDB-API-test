import requests
from endpoints.base_api_client import APIBaseClient

class TopRatedMoviesClient(APIBaseClient):
    def get(self, page = None, language = None, include_api_key = True):
        params = {}
        
        if include_api_key:
            params["api_key"] = self.api_key
        
        if page is not None: 
            params["page"] = page

        if language is not None:
            params["language"] = language

        response = requests.get(
            f"{self.base_url}/movie/top_rated", params=params
        )
        return response