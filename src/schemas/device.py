"""
Pydantic models for Device like entities
"""
from pydantic import BaseModel as PydanticBase


class DeviceBase(PydanticBase):
    name: str | None = None

    class Config:
        orm_mode = True


class DeviceCreate(DeviceBase):
    id_device_profile: int


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


class DeviceVendorCreate(DeviceBase):
    pass


class DeviceModelShow(DeviceBase):
    id: int
    pass


class DeviceModelCreate(DeviceBase):
    pass


class DeviceProfileShow(DeviceBase):
    id: int
    id_device_type: int
    id_device_model: int
    id_device_vendor: int
