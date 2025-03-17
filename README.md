[![Run tests](https://github.com/evitiska/TMDB-API-test/actions/workflows/runtests.yml/badge.svg?branch=main&event=push)](https://github.com/evitiska/TMDB-API-test/actions/workflows/runtests.yml)
### TMDB API Test

This repository contains some API tests for two endpoints on the TMDB API :
- [get-top-rated-movies](https://developers.themoviedb.org/3/movies/get-top-rated-movies)
- [rate-movie](https://developers.themoviedb.org/3/movies/rate-movie)

These tests are using [pytest](https://docs.pytest.org/en/stable/). Additional JSON schema validation is done using [jsonschema](https://python-jsonschema.readthedocs.io/en/stable/). 

### Running the tests
##
- Run them containerized with the supplied Dockerfil
