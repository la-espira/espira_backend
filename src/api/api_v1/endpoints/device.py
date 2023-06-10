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
    devices = get_items_by_model(db=db, model=Device, skip=skip, limit=limit)
    return devices


@router.get("/type", response_model=List[DeviceTypeShow])
def read_device_types(
    db: Session = Depends(get_db), skip: int = 0, limit: int = 100,
):
    """
    Retrieve devices
    """
    devices = get_items_by_model(db=db, model=DeviceType, skip=skip, limit=limit)
    return devices


@router.get("/vendor", response_model=List[DeviceVendorShow])
def read_device_vendors(
    db: Session = Depends(get_db), skip: int = 0, limit: int = 100,
):
    """
    Retrieve devices
    """
    devices = get_items_by_model(db=db, model=DeviceVendor, skip=skip, limit=limit)
    return devices


@router.get("/model", response_model=List[DeviceModelShow])
def read_device_models(
    db: Session = Depends(get_db), skip: int = 0, limit: int = 100,
):
    """
    Retrieve devices
    """
    devices = get_items_by_model(db=db, model=DeviceModel, skip=skip, limit=limit)
    return devices


@router.get("/device-profile", response_model=List[DeviceProfileShow])
def read_device_profiles(
    db: Session = Depends(get_db), skip: int = 0, limit: int = 100,
):
    """
    Retrieve devices
    """
    devices = get_items_by_model(db=db, model=DeviceProfile, skip=skip, limit=limit)
    return devices
