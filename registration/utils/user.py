from random import randint


def generate_username() -> str:
    username = "User"

    for _ in range(0, 8):
        username += str(randint(0, 9))

    return username
