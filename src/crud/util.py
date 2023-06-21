from typing import Type

from sqlalchemy import select
from sqlalchemy.engine.result import Sequence
from sqlalchemy.exc import IntegrityError

from common.log import logger
from db.session import AsyncSession as Session
from db.models.base import Base
from schemas.device import PydanticBase, DeviceBase


async def get_items_by_model(
        async_session: Session, table_model: Type[Base], skip: int = 0, limit: int = 100
) -> Sequence:
    """
    Get records from table with model
    :param async_session: Session
    :param table_model: SQLAlchemy model
    :param skip: Offset
    :param limit: Limit
    :return:
    """
    async with async_session() as session:
        stmt = select(table_model).offset(skip).limit(limit)
        # items: Sequence = db.scalars(stmt).all()
        result = await session.execute(stmt)
        items = result.scalars().all()
        logger.debug(f"Returning: {len(items)} items of {table_model}")
        return items


async def add_item_by_model(
        async_session: Session, item: PydanticBase, table_model: Type[Base]
) -> Base | None:
    """
    Add record to table with model
    :param async_session: Session
    :param item:
    :param table_model: SQLAlchemy model
    :return:
    """
    item_object: Base = table_model(**item.dict())
    logger.debug(f"Prepared item: {item_object}")
    async with async_session() as session:
        session.add(item_object)
        try:
            await session.commit()
        except IntegrityError as e:
            logger.debug(f"Failed to add item: {item_object}: IntegrityError: {e}")
            await session.rollback()
        except Exception as e:
            logger.debug(f"Failed to add item: {e}")
            await session.rollback()
        else:
            await session.refresh(item_object)
            logger.debug(f"Inserted item: {item_object}")
            return item_object
        return None
