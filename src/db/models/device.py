"""
Sqlalchemy Device like entities models
"""
from typing import List, Set

from db.models.base import Base
from sqlalchemy import String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import mapped_column, Mapped, relationship


class Device(Base):
    """
    Devices
    """
    __table_args__ = (
        {'comment': 'Devices'},
    )
    name: Mapped[str] = mapped_column(String(1024), nullable=False)
    id_device_profile: Mapped[int] = mapped_column(
        ForeignKey("t_device_profile.id")
    )


class DeviceType(Base):
    """
    Types of devices
    """
    __table_args__ = (
        {'comment': 'Device Types'},
    )
    name: Mapped[str] = mapped_column(String(1024), unique=True, nullable=False)


class DeviceModel(Base):
    """
    Models (variants/versions) of devices.
    Example: Xiaomi Mi Band 7
    """
    __table_args__ = ({'comment': 'Device Models'})
    name: Mapped[str] = mapped_column(String(1024), unique=True, nullable=False)


class DeviceVendor(Base):
    """
    Vendors of devices
    """
    __table_args__ = ({'comment': 'Device Vendors'})
    name: Mapped[str] = mapped_column(String(1024), unique=True, nullable=False)


class DeviceProfile(Base):
    """
    Profiles of devices
    """
    __table_args__ = ({'comment': 'Device Profiles'})
    name: Mapped[str] = mapped_column(String(1024), unique=True, nullable=False)
    devices: Mapped[List["Device"]] = relationship(back_populates="t_device")
    id_device_type: Mapped[int] = mapped_column(ForeignKey("t_device_type.id"))
    id_device_model: Mapped[int] = mapped_column(ForeignKey("t_device_model.id"))
    id_device_vendor: Mapped[int] = mapped_column(ForeignKey("t_device_vendor.id"))
    device_profile_parameters: Mapped[List["DeviceProfileParameter"]] = relationship(
        back_populates="t_device_profile_parameter.id"
    )


class DeviceProfileParameter(Base):
    """
    Parameters in device profile
    """
    __table_args__ = (
        UniqueConstraint("name", "id_device_profile"),
        {'comment': 'Parameters in Device Profile'}
    )
    name: Mapped[str] = mapped_column(String(1024), nullable=False)
    id_device_profile: Mapped[int] = mapped_column(ForeignKey("t_device_profile.id"))
    id_parameter_type: Mapped[int] = mapped_column(ForeignKey("t_parameter_type.id"))
