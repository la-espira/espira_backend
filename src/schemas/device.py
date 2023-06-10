"""
Pydantic models for Device like entities
"""
from pydantic import BaseModel


class DeviceBase(BaseModel):
    id: int
    name: str | None = None

    class Config:
        orm_mode = True


class DeviceShow(DeviceBase):
    id: int
    id_device_profile: int


class DeviceTypeShow(DeviceBase):
    pass


class DeviceVendorShow(DeviceBase):
    pass


class DeviceModelShow(DeviceBase):
    pass


class DeviceProfileShow(DeviceBase):
    id_device_type: int
    id_device_model: int
    id_device_vendor: int
