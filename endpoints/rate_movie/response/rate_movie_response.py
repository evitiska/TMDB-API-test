RATED_MOVIE_RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "success": {"type": "boolean"},
        "status_code": {"type": "integer"},
        "status_message": {"type": "string"}
    },
    "required": ["success", "status_code", "status_message"]
}