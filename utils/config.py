import os
from dotenv import load_dotenv
load_dotenv()

BASE_URL = "https://api.themoviedb.org/3"
API_KEY = os.getenv("TMDB_API_KEY")

# https://www.themoviedb.org/movie/939243-sonic-the-hedgehog-3
TEST_MOVIE_ID = 939243