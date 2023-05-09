import os

from common.tool import make_connection_string


DB_CONNECTION_STRING: str = os.getenv('DB_CONNECTION_STRING')
if not DB_CONNECTION_STRING:
    POSTGRES_USER: str = os.getenv('POSTGRES_USER', 'espira')
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD', 'espira')
    POSTGRES_DB: str = os.getenv('POSTGRES_DB', 'espira')
    POSTGRES_SERVER: str = os.getenv('POSTGRES_SERVER', 'localhost')
    POSTGRES_PORT: str = os.getenv('POSTGRES_PORT', '5432')
    DB_CONNECTION_STRING = make_connection_string(
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        server=POSTGRES_SERVER,
        port=POSTGRES_PORT,
        db=POSTGRES_DB,
    )


class Settings:
    def __init__(self):
        self.db_connection_string: str = DB_CONNECTION_STRING


settings = Settings()
