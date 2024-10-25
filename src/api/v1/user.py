from fastapi import APIRouter, status, Depends, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError

from model.user import User
from core.deps import get_current_user
from core.security import generate_hash_password
from core.auth import authenticate, create_token_access
from core.database import SessionLocal
from schema.user_schema import UserSchemaCreate, UserSchemaBase
from core.deps import get_session


from repository.user_repository import UserRepository

router = APIRouter()

@router.get('/logado')
def get_logado(User_logado: User = Depends(get_current_user)):
    return User_logado

@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=UserSchemaBase)
async def post_User(user: UserSchemaCreate, db: SessionLocal = Depends(get_session)):

    try:
        new_user: User = User(**user.dict())
        UserRepository.save(db, new_user)
        return new_user;
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail='Já existe um usuário com este email cadastrado.')

@router.post('/login')
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: SessionLocal = Depends(get_session)):
    user = await authenticate(mail=form_data.username, password=form_data.password , db=db)

    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Dados de acesso incorretos.')
    return JSONResponse(content={"access_token": create_token_access(sub=user.id), "token_type": "bearer"}, status_code=status.HTTP_200_OK)
