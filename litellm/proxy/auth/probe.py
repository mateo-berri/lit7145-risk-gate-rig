def check(token: str) -> bool:
    return token.startswith("sk-")


def check_admin(token: str) -> bool:
    return token.startswith("sk-admin-")
