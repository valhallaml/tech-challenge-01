import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    load_dotenv()

    API_V1_STR: str = '/api/v1'
    JWT_SECRET: str = os.getenv('JWT_SECRET')
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True

settings: Settings = Settings()

