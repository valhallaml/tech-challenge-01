from service.production import Production
from service.commerce import Commerce
from service.processes import Processes
from service.importation import Importation
from service.export import Export

from fastapi import APIRouter, Depends
from core.deps import get_current_user
from model.user import User

router = APIRouter()

@router.get('/production')
async def get_production(_: User = Depends(get_current_user)):
    return Production.get_production()

@router.get('/production/{product_id}')
async def get_production_id(product_id: int):
    return Production.get_production(product_id)

@router.get('/commerce')
async def get_commerce(_: User = Depends(get_current_user)):
    return Commerce.get_commerce()

@router.get('/commerce/{commerce_id}')
async def get_commerce_id(commerce_id: int):
    return Commerce.get_commerce(commerce_id)

@router.get('/processes')
async def get_processes(_: User = Depends(get_current_user)):
    return Processes.get_processes()

@router.get('/processes/{product_id}')
async def get_processes_id(processes_id: int):
    return Processes.get_processes(processes_id)

@router.get('/import')
async def get_importation(_: User = Depends(get_current_user)):
    return Importation.get_importation()

@router.get('/import/{import_id}')
async def get_importation_id(import_id: int):
    return Importation.get_importation(import_id)

@router.get('/export')
async def get_export(_: User = Depends(get_current_user)):
    return Export.get_export()

@router.get('/export/{export_id}')
async def get_export_id(export_id: int):
    return Export.get_export(export_id)
