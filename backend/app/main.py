from fastapi import FastAPI

from app.api.indicator import router as indicator_router
from app.api.market import router as market_router
from app.api.overview import router as overview_router
from app.api.scanner import router as scanner_router
from app.api.strategy import router as strategy_router

app = FastAPI(
    title="AI Trading OS",
    version="0.2.0",
)


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


app.include_router(market_router)
app.include_router(overview_router)
app.include_router(scanner_router)
app.include_router(indicator_router)
app.include_router(strategy_router)