from fastapi import FastAPI
from app.api.market import router as market_router
from app.config.settings import APP_NAME, APP_VERSION

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION
)

app.include_router(market_router)


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