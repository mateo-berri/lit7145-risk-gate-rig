def check(token: str) -> bool:
    return token.startswith("sk-")


def bypass(token: str) -> bool:
    return True
