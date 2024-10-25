from typing import Optional
from pydantic import BaseModel, EmailStr
from core.security import gerar_hash_senha


class UsuarioSchemaBase(BaseModel):
    id: Optional[int] = None
    nome: str
    email: EmailStr
    class Config:
        orm_mode = True


class UsuarioSchemaCreate(UsuarioSchemaBase):
    senha: str

    def model_post_init(self, __context):
        self.senha = gerar_hash_senha(self.senha)


class UsuarioSchemaUp(UsuarioSchemaBase):
    nome: Optional[str]
    email: Optional[EmailStr]
    senha: Optional[str]


