from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "FastAPI Workshop"


@lru_cache()
def get_settings():
    return Settings()
