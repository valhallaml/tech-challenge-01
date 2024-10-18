from fastapi import FastAPI

app = FastAPI(
    title = "API Embrapa's viticulture",
    description = "API to analyze Embrapa's viticulture data",
    summary = '',
    version = '1.0.0'
)

@app.get('/')
async def root():
    return { "message": "Hello World" }
