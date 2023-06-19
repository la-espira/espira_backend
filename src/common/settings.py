import os

from common.tool import make_connection_string


class Settings:
    def __init__(self):
        self.PROJECT_NAME: str = os.getenv('PROJECT_NAME', 'espira')
        with open('VERSION', 'r') as f:
            self.PROJECT_VERSION: str = f.readline().strip()

        self.DB_DEVICE_SCHEMA: str = os.getenv('DB_DEVICE_SCHEMA', 'public')
        self.DB_CONNECTION_STRING: str = os.getenv('DB_CONNECTION_STRING')
        if not self.DB_CONNECTION_STRING:
            POSTGRES_USER: str = os.getenv('POSTGRES_USER', 'espira')
            POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD', 'espira')
            POSTGRES_DB: str = os.getenv('POSTGRES_DB', 'espira')
            POSTGRES_SERVER: str = os.getenv('POSTGRES_SERVER', 'localhost')
            POSTGRES_PORT: str = os.getenv('POSTGRES_PORT', '5432')
            self.DB_CONNECTION_STRING = make_connection_string(
                user=POSTGRES_USER,
                password=POSTGRES_PASSWORD,
                server=POSTGRES_SERVER,
                port=POSTGRES_PORT,
                db=POSTGRES_DB,
            )
        self.API_V1_STR: str = os.getenv('API_V1_STR', '/api/v1')

        self.LIMIT: int = int(os.getenv('LIMIT', 100))

        self.MONGO_DB: str = os.getenv('MONGO_DB', 'espira')
        self.MONGO_USERNAME: str = os.getenv('MONGO_USERNAME', 'espira')
        self.MONGO_PASSWORD: str = os.getenv('MONGO_PASSWORD', 'espira')


settings = Settings()
