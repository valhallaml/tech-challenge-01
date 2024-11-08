from typing import Optional
from pydantic import BaseModel, EmailStr
from core.security import generate_hash_password


class UserSchemaBase(BaseModel):
    id: Optional[int] = None
    username: str
    mail: EmailStr
    class Config:
        from_attributes = True


class UserSchemaCreate(UserSchemaBase):
    password: str

    def model_post_init(self, __context):
        self.password = generate_hash_password(self.password)


class UserSchemaUp(UserSchemaBase):
    nome: Optional[str]
    username: Optional[EmailStr]
    password: Optional[str]


