"""
Sqlalchemy Parameter like entities models
"""
from typing import List
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey
from db.models import Base


class ParameterType(Base):
    """
    Types of parameters
    """
    name: Mapped[str] = mapped_column(String(1024), unique=True, nullable=False)
    table_name: Mapped[str] = mapped_column(String(1024))


class ParameterContent(Base):
    """
    Content of a parameter
    """
    name: Mapped[str] = mapped_column(String(1024), nullable=False)
    id_parameter_type: Mapped[int] = mapped_column(
        ForeignKey("t_parameter_type.id")
    )
    column_name: Mapped[str] = mapped_column(String(1024), nullable=False)
    column_type: Mapped[str] = mapped_column(String(1024), nullable=False)
