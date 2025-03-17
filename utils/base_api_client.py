from utils.config import BASE_URL, API_KEY

class TMDBAPIClient:
    def __init__(self, api_key=None):
        self.api_key = api_key or API_KEY  # Use the passed API key or fallback to the default from config
        self.base_url = BASE_URL