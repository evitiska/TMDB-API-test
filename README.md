[![Run tests](https://github.com/evitiska/TMDB-API-test/actions/workflows/runtests.yml/badge.svg?branch=main&event=push)](https://github.com/evitiska/TMDB-API-test/actions/workflows/runtests.yml)
### TMDB API Test

This repository contains some API tests for two endpoints on the TMDB API :
- [get-top-rated-movies](https://developers.themoviedb.org/3/movies/get-top-rated-movies)
- [rate-movie](https://developers.themoviedb.org/3/movies/rate-movie)

These tests are using [pytest](https://docs.pytest.org/en/stable/). Additional JSON schema validation is done using [jsonschema](https://python-jsonschema.readthedocs.io/en/stable/). 

### Running the tests

After cloning the repo there are few options how to run the tests: 

## 1. Run Tests in a Docker Container
* Build the Docker image, for example `docker build -t tmdb-api-test .`
* Run the tests in a container `docker run tmdb-api-test` (add `--rm` to remove container after run)
* You can add additional pytest arguments, such as `-k` to specify a given test. `docker run --rm tmdb-api-test -k "<test_name>"`

## 2. Run Tests Manually
* Install dependencies `pip install -r requirements.txt`
* Run tests manually `pytest`
* To run a specific test file use command `pytest tests/<test_file_name>.py`
* To run a specific test use command `pytest -k "<test_name>"`

## 3. Run Tests using GitHub Actions
This repo is configured to run tests using GitHub Actions.

* Option 1: Push a New Commit to `main` 
* Option 2: Manually Trigger a Workflow:
  * Navigate to GitHub → Actions tab
  * Select the workflow and trigger it manually if needed    
