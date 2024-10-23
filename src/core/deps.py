from typing import Optional
from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from pydantic import BaseModel

from core.auth import oauth2_schema
from core.configs import settings
from model.usuario import Usuario
from core.database import SessionLocal

from repository.usuario_repository import UsuarioRepository


class TokenData(BaseModel):
    username: Optional[str] = None


def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_current_user(db: SessionLocal = Depends(get_session), token: str = Depends(oauth2_schema)) -> Usuario:
    credential_exception: HTTPException = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Não foi possível autenticar a credencial',
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

    usuario: Usuario = UsuarioRepository.find_by_username(token_data.username)
    if usuario is None:
        raise credential_exception

    return usuario

