def render_invalid_target(code: str) -> dict[str, str]:
    return {"error": code, "error_description": "the upstream authorization server rejected the request"}
