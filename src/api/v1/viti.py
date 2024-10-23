
from service.viti_brasil import Embrapa
from fastapi import APIRouter, Depends
from core.deps import get_current_user
from model.usuario import Usuario

router = APIRouter()

@router.get('/production')
async def get_production(usuario_logado: Usuario = Depends(get_current_user)):
    return Embrapa.get_production()

@router.get('/production/{product_id}')
async def get_production(product_id: int):
    return Embrapa.get_production(product_id)