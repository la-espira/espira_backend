from typing import Any
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship, mapped_column, Mapped

from common.tool import camel_to_snake


@as_declarative()
class Base:
    id: Mapped[int] = mapped_column(primary_key=True)
    __name__: str

    # To generate tablename from class name
    @declared_attr
    def __tablename__(cls) -> str:
        """
        Generate table name like t_class_name
        :return:
        """
        # return cls.__name__.lower()
        return "t_" + camel_to_snake(cls.__name__)
