from fastapi import FastAPI

from api.api_v1.api import api_router
from common.settings import settings


def include_router(app: FastAPI):
    app.include_router(router=api_router, prefix=settings.API_V1_STR)


def start_application():
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION,
    )
    include_router(app)
    return app


app = start_application()


