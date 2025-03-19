NEW_GUEST_SESSION_RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "success": {"type": "boolean"},
        "guest_session_id": {"type": "string"},
        "expires_at": {"type": "string"}
    },
    "required": ["success", "guest_session_id", "expires_at"]
}