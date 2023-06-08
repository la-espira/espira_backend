import os

from common.tool import make_connection_string


PROJECT_NAME: str = os.getenv('PROJECT_NAME', 'espira')
PROJECT_VERSION: str = os.getenv('PROJECT_VERSION', '0.1')
DB_CONNECTION_STRING: str = os.getenv('DB_CONNECTION_STRING')
DB_DEVICE_SCHEMA: str = os.getenv('DB_DEVICE_SCHEMA', 'public')
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
API_V1_STR: str = os.getenv('API_V1_STR', '/api/v1')


class Settings:
    def __init__(self):
        self.project_name: str = PROJECT_NAME
        self.project_version: str = PROJECT_VERSION
        self.db_connection_string: str = DB_CONNECTION_STRING
        self.api_v1_str: str = API_V1_STR


settings = Settings()
