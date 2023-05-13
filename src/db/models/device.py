"""
Sqlalchemy Device like entities models
"""
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
    Types of devices
    """
    name: Mapped[str] = mapped_column(String(1024))


class DeviceModel(Base):
    """
    Models of devices.
    Example: Xiaomi Mi Band 7
    """
    name: Mapped[str] = mapped_column(String(1024))


class DeviceVendor(Base):
    """
    Vendors of devices
    """
    name: Mapped[str] = mapped_column(String(1024))


class DeviceProfile(Base):
    """
    Profiles of devices
    """
    name: Mapped[str] = mapped_column(String(1024))
    devices: Mapped[List["Device"]] = relationship(back_populates="t_device")
    id_type: Mapped[int] = mapped_column(ForeignKey("t_device_type.id"))
    id_device_model: Mapped[int] = mapped_column(ForeignKey("t_device_model.id"))
    id_device_vendor: Mapped[int] = mapped_column(ForeignKey("t_device_vendor.id"))
    device_profile_parameters: Mapped[List["DeviceProfileParameter"]] = relationship(
        back_populates="t_device_profile_parameter.id"
    )


class DeviceProfileParameter(Base):
    """
    Parameters in device profile
    """
    name: Mapped[str] = mapped_column(String(1024))
    id_device_profile: Mapped[int] = mapped_column(ForeignKey("t_device_profile.id"))
