MOVIE_ITEM_SCHEMA = {
    "type": "object",
    "properties": {
        "adult": { "type": "boolean" },
        "backdrop_path": { "type": "string" },
        "genre_ids": {
            "type": "array",
            "items": { "type": "integer" }
        },
        "id": { "type": "integer" },
        "original_language": { "type": "string" },
        "original_title": { "type": "string" },
        "overview": { "type": "string" },
        "popularity": { "type": "number" },
        "poster_path": { "type": "string" },
        "release_date": { "type": "string", "format": "date" },
        "title": { "type": "string" },
        "video": { "type": "boolean" },
        "vote_average": { "type": "number" },
        "vote_count": { "type": "integer" }
    },
    "required": [
        "adult", "backdrop_path", "genre_ids", "id", "original_language", 
        "original_title", "overview", "popularity", "poster_path", "release_date", 
        "title", "video", "vote_average", "vote_count"
    ]
}

TOP_RATED_MOVIES_RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "page": {"type": "integer"},
        "results": {
            "type": "array",
            "items": MOVIE_ITEM_SCHEMA
        }
    },
    "required": ["page", "results"]
}