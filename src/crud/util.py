from typing import Type

from sqlalchemy import select
from sqlalchemy.engine.result import Sequence
from sqlalchemy.orm import Session

from common.log import logger
from db.models.base import Base


def get_items_by_model(
        db: Session, model: Type[Base], skip: int = 0, limit: int = 100
) -> Sequence:
    """
    Get records from table with model
    :param db: Session
    :param model: SQLAlchemy model
    :param skip: Offset
    :param limit: Limit
    :return:
    """
    stmt = select(model).offset(skip).limit(limit)
    # items: Sequence = db.scalars(stmt).all()
    items: Sequence = db.execute(stmt).scalars().all()
    logger.debug(f"Returning: {len(items)} items of {model}")
    return items

