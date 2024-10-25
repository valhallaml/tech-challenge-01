from fastapi import APIRouter, status, Depends, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse


from model.usuario import Usuario
from core.deps import get_current_user
from core.security import gerar_hash_senha
from core.auth import autenticar, criar_token_acesso
from core.database import SessionLocal
from schema.usuario_schema import UsuarioSchemaCreate, UsuarioSchemaBase
from core.deps import get_session
from sqlalchemy.exc import IntegrityError

from repository.usuario_repository import UsuarioRepository

router = APIRouter()

@router.get('/logado')
def get_logado(usuario_logado: Usuario = Depends(get_current_user)):
    return usuario_logado

@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=UsuarioSchemaBase)
async def post_usuario(usuario: UsuarioSchemaCreate, db: SessionLocal = Depends(get_session)):

    try:
        novo_usuario: Usuario = Usuario(**usuario.dict())
        UsuarioRepository.save(db, novo_usuario)
        return novo_usuario;
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail='Já existe um usuário com este email cadastrado.')

@router.post('/login')
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: SessionLocal = Depends(get_session)):
    usuario = await autenticar(email=form_data.username, senha=form_data.password , db=db)

    if not usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Dados de acesso incorretos.')
    return JSONResponse(content={"access_token": criar_token_acesso(sub=usuario.id), "token_type": "bearer"}, status_code=status.HTTP_200_OK)
