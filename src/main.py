import os
import uvicorn

from fastapi import FastAPI

from api.router import api_router
from core.database import Base, engine
from core.configs import settings

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title = "API Embrapa's viticulture",
    description = "API to analyze Embrapa's viticulture data",
    summary = '',
    version = '1.0.0'
)

app.include_router(api_router,prefix=settings.API_V1_STR)

if __name__ == '__main__':
    environment = os.getenv('ENVIRONMENT', 'development')
    is_dev = environment == 'development'
    uvicorn.run(app='main:app', host="0.0.0.0", port=8000, reload=is_dev)
