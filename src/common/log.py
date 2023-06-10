import os
import sys
from loguru import logger

LOG_LEVEL: str = os.getenv('LOG_LEVEL', 'INFO')
LOGURU_FORMAT: str = os.getenv(
    'LOGURU_FORMAT',
    "<level>{level}</level> | " 
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | " 
    "<cyan>{module}</cyan> | " 
    "<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
)

logger.remove()
error_handler = logger.add(
    sys.stderr,
    level=LOG_LEVEL,
    format=LOGURU_FORMAT
)
logger.debug(f"Log level set from env: {LOG_LEVEL}")
