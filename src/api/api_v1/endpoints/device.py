from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from common.settings import settings
from crud.util import get_items_by_model, add_item_by_model
from db.models.device import *
from db.session import get_db
from schemas.device import *
from common.log import logger

router = APIRouter()


@router.get("/all", response_model=List[DeviceShow])
def read_devices(
    db: Session = Depends(get_db), skip: int = 0, limit: int = settings.LIMIT,
):
    """
    Get devices
    - **skip**: Start with
    - **limit**: Amount to get
    \f
    :param db: Session
    :param skip: Offset
    :param limit: Limit
    :return:
    """
    devices = get_items_by_model(db=db, model=Device, skip=skip, limit=limit)
    return devices


@router.get("/type", response_model=List[DeviceTypeShow])
def read_device_types(
    db: Session = Depends(get_db), skip: int = 0, limit: int = settings.LIMIT,
):
    """
    Retrieve devices
    """
    devices = get_items_by_model(db=db, model=DeviceType, skip=skip, limit=limit)
    return devices


@router.post("/type/create/", response_model=DeviceTypeShow)
def create_device_type(device_type: DeviceTypeCreate, db: Session = Depends(get_db)):
    logger.debug(f"Post item: {device_type}")
    new_element = add_item_by_model(item=device_type, model=DeviceType, db=db)
    return new_element


@router.get("/vendor", response_model=List[DeviceVendorShow])
def read_device_vendors(
    db: Session = Depends(get_db), skip: int = 0, limit: int = settings.LIMIT,
):
    """
    Retrieve devices
    """
    devices = get_items_by_model(db=db, model=DeviceVendor, skip=skip, limit=limit)
    return devices


@router.get("/model", response_model=List[DeviceModelShow])
def read_device_models(
    db: Session = Depends(get_db), skip: int = 0, limit: int = settings.LIMIT,
):
    """
    Retrieve devices
    """
    devices = get_items_by_model(db=db, model=DeviceModel, skip=skip, limit=limit)
    return devices


@router.get("/device-profile", response_model=List[DeviceProfileShow])
def read_device_profiles(
    db: Session = Depends(get_db), skip: int = 0, limit: int = settings.LIMIT,
):
    """
    Retrieve devices
    """
    devices = get_items_by_model(db=db, model=DeviceProfile, skip=skip, limit=limit)
    return devices
