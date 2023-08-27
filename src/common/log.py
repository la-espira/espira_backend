import sys

from loguru import logger
from pydantic_settings import BaseSettings


class LogSettings(BaseSettings):
    log_level: str = 'INFO'
    loguru_format: str = (
        "<level>{level}</level> | " 
        "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | " 
        "<cyan>{module}</cyan> | " 
        "<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
    )


log_settings = LogSettings()
logger.remove()
error_handler = logger.add(
    sys.stderr,
    level=log_settings.log_level,
    format=log_settings.loguru_format,
)
logger.debug(f"Log level set from env: {log_settings.log_level}")
