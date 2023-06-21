from typing import Annotated, AsyncIterator

from fastapi import Depends
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from common.log import logger
from common.settings import settings

async_engine = create_async_engine(
    settings.DB_CONNECTION_STRING,
    pool_pre_ping=True,     # TODO ?
    future=True,            # TODO ?
    # autoflush=False,      # TODO ?
    echo=True,              # TODO For debugging
)

async_session = async_sessionmaker(
    bind=async_engine,
    # autoflush=False,
    # future=True,
    expire_on_commit=False,
    # class_=AsyncSession,
)


async def get_db() -> AsyncIterator[async_sessionmaker]:
    try:
        yield async_session
    except SQLAlchemyError as e:
        logger.exception(f"Failed to create async session: {e}")
    finally:
        pass

AsyncSession = Annotated[async_sessionmaker, Depends(get_db)]


# def get_db() -> Generator:
#     try:
#         db = SessionLocal()
#         yield db
#     finally:
#         db.close()
