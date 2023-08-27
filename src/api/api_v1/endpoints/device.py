from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from common.log import logger
from common.settings import settings
from crud.util import get_items_by_model, add_item_by_model
from db.models.device import *
from db.pg_session import get_db
from schemas.device import *

router = APIRouter()


@router.get("", response_model=List[DeviceShow])
async def read_devices(
    db: Session = Depends(get_db), skip: int = 0, limit: int = settings.limit,
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
    devices = await get_items_by_model(async_session=db, table_model=Device, skip=skip, limit=limit)
    return devices


@router.post("", response_model=DeviceCreate)
async def create_device(device: DeviceCreate, db: Session = Depends(get_db)):
    """
    Create a Device Type
    """
    logger.debug(f"Post item: {device}")
    new_element = await add_item_by_model(item=device, table_model=Device, async_session=db)
    if new_element:
        return new_element
    else:
        raise HTTPException(status_code=400,detail="Already exists",)


@router.get("/type", response_model=List[DeviceTypeShow])
async def read_device_types(
    db: Session = Depends(get_db), skip: int = 0, limit: int = settings.limit,
):
    """
    Retrieve devices
    """
    devices = await get_items_by_model(async_session=db, table_model=DeviceType, skip=skip, limit=limit)
    return devices


@router.post("/type/create/", response_model=DeviceTypeShow)
async def create_device_type(device_type: DeviceTypeCreate, db: Session = Depends(get_db)):
    """
    Create a Device Type
    """
    logger.debug(f"Post item: {device_type}")
    new_element = await add_item_by_model(item=device_type, table_model=DeviceType, async_session=db)
    if new_element:
        return new_element
    else:
        raise HTTPException(status_code=400, detail="Already exists",)


@router.get("/vendor", response_model=List[DeviceVendorShow])
async def read_device_vendors(
    db: Session = Depends(get_db), skip: int = 0, limit: int = settings.limit,
):
    """
    Retrieve devices
    """
    devices = await get_items_by_model(async_session=db, table_model=DeviceVendor, skip=skip, limit=limit)
    return devices


@router.post("/vendor/create/", response_model=DeviceVendorShow)
async def create_device_vendor(device_vendor: DeviceVendorCreate, db: Session = Depends(get_db)):
    """
    Create a Device Vendor
    """
    logger.debug(f"Post item: {device_vendor}")
    new_element = await add_item_by_model(
        item=device_vendor, table_model=DeviceVendor, async_session=db
    )
    if new_element:
        return new_element
    else:
        raise HTTPException(status_code=400, detail="Already exists",)


@router.get("/model", response_model=List[DeviceModelShow])
async def read_device_models(
    db: Session = Depends(get_db), skip: int = 0, limit: int = settings.limit,
):
    """
    Retrieve devices
    """
    devices = await get_items_by_model(async_session=db, table_model=DeviceModel, skip=skip, limit=limit)
    return devices


@router.post("/model/create/", response_model=DeviceModelShow)
async def create_device_model(device_model: DeviceModelCreate, db: Session = Depends(get_db)):
    """
    Create a Device Vendor
    """
    logger.debug(f"Post item: {device_model}")
    new_element = await add_item_by_model(
        item=device_model, table_model=DeviceModel, async_session=db
    )
    if new_element:
        return new_element
    else:
        raise HTTPException(status_code=400, detail="Already exists",)


@router.get("/device-profile", response_model=List[DeviceProfileShow])
async def read_device_profiles(
    db: Session = Depends(get_db), skip: int = 0, limit: int = settings.limit,
):
    """
    Retrieve devices
    """
    devices = await get_items_by_model(async_session=db, table_model=DeviceProfile, skip=skip, limit=limit)
    return devices


@router.post("/device-profile/create", response_model=DeviceProfileShow)
async def create_device_profiles(
        device_model: DeviceProfileCreate,
        db: Session = Depends(get_db),
):
    """
    Create device profile
    """
    logger.debug(f"Post item: {device_model}")
    new_element = await add_item_by_model(
        item=device_model, table_model=DeviceProfile, async_session=db
    )
    if new_element:
        return new_element
    else:
        raise HTTPException(status_code=400, detail="Already exists",)
