
from src.service.viti_brasil import Embrapa
from fastapi import APIRouter

router = APIRouter()

@router.get('/production')
async def get_production():
    return Embrapa.get_production()

@router.get('/production/{product_id}')
async def get_production(product_id: int):
    return Embrapa.get_production(product_id)
