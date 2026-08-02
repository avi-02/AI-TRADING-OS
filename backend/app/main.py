from fastapi import FastAPI

from app.api.market import router as market_router
from app.api.overview import router as overview_router

app = FastAPI(
    title="AI Trading OS",
    version="0.2.0"
)

app.include_router(market_router)
app.include_router(overview_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Trading OS 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "running"
    }