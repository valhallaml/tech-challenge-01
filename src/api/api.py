from fastapi import APIRouter
from api.v1 import viti
from api.v1 import usuario

api_router = APIRouter()
api_router.include_router(viti.router, prefix='/viti', tags=["vitis"])
api_router.include_router(usuario.router, prefix='/usuario', tags=["usuarios"])