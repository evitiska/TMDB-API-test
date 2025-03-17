import requests
from utils.base_api_client import TMDBAPIClient

class TopRatedMoviesTMDBAPIClient(TMDBAPIClient):
    def get(self, page = None, language = None):
        params = {"api_key": self.api_key}
        
        if page is not None: 
            params["page"] = page

        if language is not None:
            params["language"] = language

        response = requests.get(
            f"{self.base_url}/movie/top_rated", params=params
        )
        return response