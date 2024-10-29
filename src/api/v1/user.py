from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError

from src.model.user import User
from src.core.deps import get_current_user
from src.core.auth import authenticate, create_token_access
from src.core.database import SessionLocal
from src.schema.user_schema import UserSchemaCreate, UserSchemaBase
from src.core.deps import get_session


from src.repository.user_repository import UserRepository

router = APIRouter()

@router.get('/logged')
def get_logged(user: User = Depends(get_current_user)):
    return {
        'username': user.username,
        'main': user.mail
    }

@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=UserSchemaBase)
async def post_user(user: UserSchemaCreate, db: SessionLocal = Depends(get_session)):

    try:
        new_user: User = User(**user.dict())
        UserRepository.save(db, new_user)
        return new_user
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail='There is already a user with this email registered.')

@router.post('/login')
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: SessionLocal = Depends(get_session)):
    user = await authenticate(mail=form_data.username, password=form_data.password , db=db)

    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Incorrect access data.')
    return JSONResponse(content={"access_token": create_token_access(sub=user.username), "token_type": "bearer"}, status_code=status.HTTP_200_OK)
