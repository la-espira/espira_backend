"""
Pydantic models for Device like entities
"""
from pydantic import BaseModel


class DeviceBase(BaseModel):
    name: str | None = None


class DeviceShow(DeviceBase):
    pass
