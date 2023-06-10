from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.util import get_items_by_model
from db.models.device import *
from db.session import get_db
from schemas.device import *

router = APIRouter()


@router.get("/all", response_model=List[DeviceShow])
def read_devices(
    db: Session = Depends(get_db), skip: int = 0, limit: int = 100,
):
    """
    Retrieve devices
    """
    devices = get_items_by_model(db=db, model=Device)
    return devices


@router.get("/type", response_model=List[DeviceTypeShow])
def read_device_types(
    db: Session = Depends(get_db), skip: int = 0, limit: int = 100,
):
    """
    Retrieve devices
    """
    devices = get_items_by_model(db=db, model=DeviceType)
    return devices


@router.get("/vendor", response_model=List[DeviceVendorShow])
def read_device_vendors(
    db: Session = Depends(get_db), skip: int = 0, limit: int = 100,
):
    """
    Retrieve devices
    """
    devices = get_items_by_model(db=db, model=DeviceVendor)
    return devices


@router.get("/model", response_model=List[DeviceModelShow])
def read_device_vendors(
    db: Session = Depends(get_db), skip: int = 0, limit: int = 100,
):
    """
    Retrieve devices
    """
    devices = get_items_by_model(db=db, model=DeviceModel)
    return devices


@router.get("/device-profile", response_model=List[DeviceProfileShow])
def read_device_vendors(
    db: Session = Depends(get_db), skip: int = 0, limit: int = 100,
):
    """
    Retrieve devices
    """
    devices = get_items_by_model(db=db, model=DeviceProfile)
    return devices
