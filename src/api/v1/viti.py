
from src.service.viti_brasil import Embrapa
from fastapi import APIRouter, Depends
from src.core.deps import get_current_user
from src.model.user import User

router = APIRouter()

@router.get('/production')
async def get_production(User_logado: User = Depends(get_current_user)):
    return Embrapa.get_production()

@router.get('/production/{product_id}')
async def get_production(product_id: int):
    return Embrapa.get_production(product_id)