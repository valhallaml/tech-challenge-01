from pytz import timezone

from typing import Optional, List
from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer

from jose import jwt

from model.usuario import Usuario
from core.configs import settings
from core.security import verificar_senha
from pydantic import EmailStr


oauth2_schema = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/usuarios/login"
)


async def autenticar(email: EmailStr, senha: str) -> Optional[Usuario]:
        usuario = Usuario()
        usuario.nome = "admin"
        usuario.email = "admin@viti.com"
        usuario.senha = "123456"

        if not usuario:
            return None

        if not verificar_senha(senha, usuario.senha):
            return None
        return usuario


def _criar_token(tipo_token: str, tempo_vida: timedelta, sub: str) -> str:
    payload = {}

    sp = timezone('America/Sao_Paulo')
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
