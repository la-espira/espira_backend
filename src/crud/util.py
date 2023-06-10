from typing import Type

from sqlalchemy import select
from sqlalchemy.engine.result import Sequence
from sqlalchemy.orm import Session

from common.log import logger
from db.models.base import Base


def get_items_by_model(
        db: Session, model: Type[Base], skip: int = 0, limit: int = 100
) -> Sequence:
    """"
    Get records for table with model
    """
    stmt = select(model)
    items: Sequence = db.scalars(stmt).all()
    logger.debug(f"Returning: {len(items)} items of {model}")
    return items

