"""
Sqlalchemy Device like entities models
"""
from typing import List, Set
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, ForeignKey, UniqueConstraint
from db.models import Base


class Device(Base):
    """
    Devices
    """
    name: Mapped[str] = mapped_column(String(1024), nullable=False)
    id_device_profile: Mapped[int] = mapped_column(
        ForeignKey("t_device_profile.id")
    )


class DeviceType(Base):
    """
    Types of devices
    """
    name: Mapped[str] = mapped_column(String(1024), unique=True, nullable=False)


class DeviceModel(Base):
    """
    Models (variants/versions) of devices.
    Example: Xiaomi Mi Band 7
    """
    name: Mapped[str] = mapped_column(String(1024), unique=True, nullable=False)


class DeviceVendor(Base):
    """
    Vendors of devices
    """
    name: Mapped[str] = mapped_column(String(1024), unique=True, nullable=False)


class DeviceProfile(Base):
    """
    Profiles of devices
    """
    name: Mapped[str] = mapped_column(String(1024), unique=True, nullable=False)
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
    __table_args__ = (
        UniqueConstraint("name", "id_device_profile"),
    )
    name: Mapped[str] = mapped_column(String(1024), nullable=False)
    id_device_profile: Mapped[int] = mapped_column(ForeignKey("t_device_profile.id"))
    id_parameter_type: Mapped[int] = mapped_column(ForeignKey("t_parameter_type.id"))
