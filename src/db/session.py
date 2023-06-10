from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from common.settings import settings

engine = create_engine(settings.DB_CONNECTION_STRING)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
