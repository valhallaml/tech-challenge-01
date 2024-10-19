from fastapi import FastAPI
from viti_brasil import Embrapa

app = FastAPI(
    title = "API Embrapa's viticulture",
    description = "API to analyze Embrapa's viticulture data",
    summary = '',
    version = '1.0.0'
)

@app.get('/')
async def root():

    data = Embrapa.get_production()

    return { "message": data.head() }
