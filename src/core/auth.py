from pytz import timezone

from typing import Optional
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer

from jose import jwt

from src.model.user import User
from src.core.configs import settings
from src.core.security import verify_password
from pydantic import EmailStr
from src.core.database import SessionLocal

from src.repository.user_repository import UserRepository

oauth2_schema = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/user/login"
)

async def authenticate(mail: EmailStr, password: str, db: SessionLocal) -> Optional[User]:
        user: User = UserRepository.find_by_mail(db, mail)
        if not user:
            return None

        if not verify_password(password, user.password):
            return None
        return user

def _create_token(type_token: str, life_time: timedelta, sub: str) -> str:
    payload = {}

    sp = timezone('America/Fortaleza')
    expires = datetime.now(tz=sp) + life_time

    payload["type"] = type_token
    payload["exp"] = expires
    payload["iat"] = datetime.now(tz=sp)
    payload["sub"] = str(sub)

    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM)

def create_token_access(sub: str) -> str:
    return _create_token(
        type_token='access_token',
        life_time=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        sub=sub
    )
