from pytz import timezone

from typing import Optional
from datetime import datetime, timedelta
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from jose import jwt

from model.usuario import Usuario
from core.configs import settings
from core.security import verificar_senha
from pydantic import EmailStr
from core.database import SessionLocal

from repository.usuario_repository import UsuarioRepository

oauth2_schema = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/usuario/login"
)


async def autenticar(email: EmailStr, senha: str, db: SessionLocal) -> Optional[Usuario]:
        usuario: Usuario = UsuarioRepository.find_by_email(db, email)
        if not usuario:
            return None

        if not verificar_senha(senha, usuario.senha):
            return None
        return usuario


def _criar_token(tipo_token: str, tempo_vida: timedelta, sub: str) -> str:
    payload = {}

    sp = timezone('America/Fortaleza')
    expira = datetime.now(tz=sp) + tempo_vida

    payload["type"] = tipo_token
    payload["exp"] = expira
    payload["iat"] = datetime.now(tz=sp)
    payload["sub"] = str(sub)

    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM)


def criar_token_acesso(sub: str) -> str:
    return _criar_token(
        tipo_token='access_token',
        tempo_vida=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        sub=sub
    )
