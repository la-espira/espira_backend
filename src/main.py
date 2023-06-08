from fastapi import FastAPI

from common.settings import settings
from api.api_v1.api import api_router


def include_router(app: FastAPI):
    app.include_router(router=api_router, prefix=settings.api_v1_str)


def start_application():
    app = FastAPI(
        title=settings.project_name,
        version=settings.project_version,
    )
    include_router(app)
    return app


app = start_application()


