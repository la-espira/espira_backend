"""
Pydantic models for Device like entities
"""
from pydantic import BaseModel


class DeviceBase(BaseModel):
    name: str | None = None

    class Config:
        orm_mode = True


class DeviceShow(DeviceBase):
    id: int
    id_device_profile: int


class DeviceTypeShow(DeviceBase):
    id: int
    pass


class DeviceTypeCreate(DeviceBase):
    pass


class DeviceVendorShow(DeviceBase):
    id: int
    pass


class DeviceModelShow(DeviceBase):
    id: int
    pass


class DeviceProfileShow(DeviceBase):
    id: int
    id_device_type: int
    id_device_model: int
    id_device_vendor: int
