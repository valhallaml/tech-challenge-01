from fastapi import APIRouter
from src.api.v1 import viti
from src.api.v1 import user

api_router = APIRouter()
api_router.include_router(viti.router, prefix='/viti', tags=["vitis"])
api_router.include_router(user.router, prefix='/user', tags=["users"])