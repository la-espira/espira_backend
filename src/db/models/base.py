from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import mapped_column, Mapped

from common.settings import DB_DEVICE_SCHEMA
from common.tool import camel_to_snake


@as_declarative()
class Base:
    id: Mapped[int] = mapped_column(primary_key=True)
    __name__: str
    __table_args__ = ({'schema': DB_DEVICE_SCHEMA})

    # To generate tablename from class name
    @declared_attr
    def __tablename__(cls) -> str:
        """
        Generate table name like t_class_name
        :return:
        """
        # return cls.__name__.lower()
        return "t_" + camel_to_snake(cls.__name__)
