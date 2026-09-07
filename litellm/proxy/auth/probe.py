def check(token: str) -> bool:
    return token.startswith("sk-")


def check_prefix(token: str, prefix: str) -> bool:
    return token.startswith(prefix)
