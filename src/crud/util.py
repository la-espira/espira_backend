from typing import Type

from sqlalchemy import select
from sqlalchemy.engine.result import Sequence
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from common.log import logger
from db.models.base import Base
from schemas.device import PydanticBase, DeviceBase


def get_items_by_model(
        db: Session, table_model: Type[Base], skip: int = 0, limit: int = 100
) -> Sequence:
    """
    Get records from table with model
    :param db: Session
    :param table_model: SQLAlchemy model
    :param skip: Offset
    :param limit: Limit
    :return:
    """
    stmt = select(table_model).offset(skip).limit(limit)
    # items: Sequence = db.scalars(stmt).all()
    items: Sequence = db.execute(stmt).scalars().all()
    logger.debug(f"Returning: {len(items)} items of {table_model}")
    return items


def add_item_by_model(
        db: Session, item: PydanticBase, table_model: Type[Base]
) -> Base | None:
    """
    Add record to table with model
    :param db: Session
    :param item:
    :param table_model: SQLAlchemy model
    :return:
    """
    item_object: Base = table_model(**item.dict())
    logger.debug(f"Prepared item: {item_object}")
    db.add(item_object)
    try:
        db.commit()
    except IntegrityError as e:
        logger.debug(f"Failed to add item: {item_object}: IntegrityError: {e}")
        db.rollback()
    except Exception as e:
        logger.debug(f"Failed to add item: {e}")
        db.rollback()
    else:
        db.refresh(item_object)
        logger.debug(f"Inserted item: {item_object}")
        return item_object
    return None
