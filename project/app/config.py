# project/app/config.py


import logging
import socket
from functools import lru_cache
from uuid import uuid4
from pydantic import BaseSettings, AnyUrl


log = logging.getLogger("uvicorn")

class Settings(BaseSettings):
    environment: str = "dev"
    id: str = str(uuid4())
    testing: bool = 0
    database_url: AnyUrl = None
    hostname: str = socket.gethostname()


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
