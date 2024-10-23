import os
import uvicorn
from fastapi import FastAPI
from service.viti_brasil import Embrapa
from api.api import api_router
from core.configs import settings
from core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title = "API Embrapa's viticulture",
    description = "API to analyze Embrapa's viticulture data",
    summary = '',
    version = '1.0.0'
)

app.include_router(api_router,prefix=settings.API_V1_STR,tags=['vitis'])
app.include_router(api_router,prefix=settings.API_V1_STR,tags=['usuarios'])

if __name__ == '__main__':
    environment = os.getenv('ENVIRONMENT', 'development')
    is_dev = environment == 'development'
    uvicorn.run(app='main:app', host="0.0.0.0", port=8000, reload=is_dev, workers=1, debug=True)
