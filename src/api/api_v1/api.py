from fastapi import APIRouter

from src.api.api_v1.endpoints import device

api_router = APIRouter()
api_router.include_router(router=device.router, prefix="/devices", tags=["devices"])
