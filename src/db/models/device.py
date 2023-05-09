from typing import List, Set
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey
from db.models import Base


class Device(Base):
    """
    Device model
    """
    name: Mapped[str] = mapped_column(String(1024))
    id_device_profile: Mapped[int] = mapped_column(
        ForeignKey("t_device_profile.id")
    )


class DeviceType(Base):
    """
    Device Type model
    """
    name: Mapped[str] = mapped_column(String(1024))


class DeviceModel(Base):
    """
    Device Model sqlalchemy model
    """
    name: Mapped[str] = mapped_column(String(1024))


class DeviceVendor(Base):
    """
    Device Vendor model
    """
    name: Mapped[str] = mapped_column(String(1024))


class DeviceProfile(Base):
    """
    Device Profile model
    """
    name: Mapped[str] = mapped_column(String(1024))
    devices: Mapped[List["Device"]] = relationship(back_populates="t_device")
    types: Mapped[List["DeviceType"]] = relationship(back_populates="t_device_type")
    models: Mapped[List["DeviceModel"]] = relationship(back_populates="t_device_model")
    vendors: Mapped[List["DeviceVendor"]] = relationship(back_populates="t_device_vendor")
