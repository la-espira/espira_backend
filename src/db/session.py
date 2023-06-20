from typing import Generator, Annotated, AsyncIterator
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker
from fastapi import Depends

from common.log import logger
from common.settings import settings

# engine = create_engine(settings.DB_CONNECTION_STRING)
async_engine = create_async_engine(
    settings.DB_CONNECTION_STRING,
    pool_pre_ping=True,     # TODO ?
    future=True,            # TODO ?
    # autoflush=False,        # TODO ?
    echo=True,              # TODO ?
)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
async_session = async_sessionmaker(
    bind=async_engine,
    # autoflush=False,
    # future=True,
    expire_on_commit=False,
    # class_=AsyncSession,
)


# def get_db() -> Generator:
#     try:
#         db = SessionLocal()
#         yield db
#     finally:
#         db.close()

async def get_db() -> AsyncIterator[async_sessionmaker]:
    # db = DBSession()
    try:
        yield async_session
    except SQLAlchemyError as e:
        logger.exception(f"Failed to create async session: {e}")
    finally:
        # db.close()
        pass

AsyncSession = Annotated[async_sessionmaker, Depends(get_db)]
