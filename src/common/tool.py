import re
from urllib.parse import quote_plus


def camel_to_snake(name: str) -> str:
    """
    Converts CamelToSnake >> camel_to_snake
    :param name: CamelString
    :return: snake_string
    """
    new_name: str = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
    return new_name


def snake_to_camel(name: str) -> str:
    """
    Converts snake_to_camel >> SnakeToCamel
    :param name: snake_string
    :return: CamelString
    """
    new_name: str = ''.join(word.title() for word in name.split('_'))
    return new_name


def make_connection_string(
        user: str,
        password: str,
        server: str,
        port: str,
        db: str,
) -> str:
    """
    Makes postgres connections string from attrs
    :param user:
    :param password:
    :param server:
    :param port:
    :param db:
    :return:
    """
    return (
        f"postgresql+asyncpg://{quote_plus(user)}:"
        f"{quote_plus(password)}@"
        f"{server}:{port}/{db}"
    )

