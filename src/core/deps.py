from typing import Optional
from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from pydantic import BaseModel

from src.core.auth import oauth2_schema
from src.core.configs import settings
from src.model.user import User
from src.core.database import SessionLocal

from src.repository.user_repository import UserRepository


class TokenData(BaseModel):
    username: Optional[str] = None


def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_current_user(db: SessionLocal = Depends(get_session), token: str = Depends(oauth2_schema)) -> User:
    credential_exception: HTTPException = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Unable to authenticate credential',
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.ALGORITHM],
            options={"verify_aud": False}
        )

        username: str = payload.get("sub")
        if username is None:
            raise credential_exception

        token_data: TokenData = TokenData(username=username)
    except JWTError:
        raise credential_exception

    user: User = UserRepository.find_by_username(db, token_data.username)
    if user is None:
        raise credential_exception

    return user

