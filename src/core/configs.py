from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    API_V1_STR: str = '/api/v1'
    JWT_SECRET: str = 'qS96E1oCfq5gEZH-ngD91NC2qkcl0cffhNTIDGpF4pw'
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True

settings: Settings = Settings()

