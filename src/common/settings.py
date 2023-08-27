from pydantic_settings import BaseSettings

from common.tool import make_connection_string


class Settings(BaseSettings):
    project_name: str = 'espira'
    project_version: str = ''

    db_device_schema: str = 'public'
    db_connection_string: str = ''
    postgres_user: str = ''
    postgres_password: str = ''
    postgres_db: str = ''
    postgres_server: str = ''
    postgres_port: str = ''

    sqlalchemy_echo: bool = False
    api_v1_str: str = '/api/v1'

    limit: int = 100

    mongo_server: str = 'localhost'
    mongo_port: int = 27017
    mongo_db: str = 'espira'
    mongo_username: str = 'espira'
    mongo_password: str = 'espira'
    mongo_connection_string: str = ''


settings = Settings()
if not settings.project_version:
    with open('VERSION', 'r') as f:
        settings.project_version = f.readline().strip()
if not settings.db_connection_string:
    settings.postgres_user = 'espira'
    settings.postgres_password = 'espira'
    settings.postgres_db = 'espira'
    settings.postgres_server = 'localhost'
    settings.postgres_port = '5432'
    settings.db_connection_string = make_connection_string(
        user=settings.postgres_user,
        password=settings.postgres_password,
        server=settings.postgres_server,
        port=settings.postgres_port,
        db=settings.postgres_db,
    )
settings.mongo_connection_string = (
    f"mongo://{settings.mongo_username}:{settings.mongo_password}"
    f"@{settings.mongo_server}:{settings.mongo_port}/{settings.mongo_db}"
)
