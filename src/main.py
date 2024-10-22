import os
import uvicorn
from fastapi import FastAPI
from viti_brasil import Embrapa

app = FastAPI(
    title = "API Embrapa's viticulture",
    description = "API to analyze Embrapa's viticulture data",
    summary = '',
    version = '1.0.0'
)

@app.get('/production')
async def get_production():
    return Embrapa.get_production()

@app.get('/production/{product_id}')
async def get_production(product_id: int):
    return Embrapa.get_production(product_id)

if __name__ == '__main__':
    environment = os.getenv('ENVIRONMENT', 'development')
    is_dev = environment == 'development'
    uvicorn.run(app='main:app', host="0.0.0.0", port=8000, reload=is_dev, workers=1)
