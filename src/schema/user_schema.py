from typing import Optional
from pydantic import BaseModel, EmailStr
from src.core.security import generate_hash_password


class UserSchemaBase(BaseModel):
    id: Optional[int] = None
    username: str
    mail: EmailStr
    class Config:
        orm_mode = True


class UserSchemaCreate(UserSchemaBase):
    password: str

    def model_post_init(self, __context):
        self.password = generate_hash_password(self.password)


class UserSchemaUp(UserSchemaBase):
    nome: Optional[str]
    username: Optional[EmailStr]
    password: Optional[str]


