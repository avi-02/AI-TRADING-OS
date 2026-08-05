from fastapi import FastAPI

from app.api.market import router as market_router
from app.api.overview import router as overview_router
from app.api.scanner import router as scanner_router
from app.api.indicator import router as indicator_router
from app.api.strategy import router as strategy_router
from app.api.backtest import router as backtest_router
from app.api.paper import router as paper_router

app = FastAPI(
    title="AI Trading OS",
    description="""
AI Trading OS is a modular algorithmic trading backend built with FastAPI.

## Features

- 📈 Live Market Data
- 🕒 Historical Candle Data
- 📊 Technical Indicators
  - SMA
  - EMA
  - RSI
  - MACD
  - Bollinger Bands
- 🔍 Market Scanner
- 🤖 Momentum Trading Strategy
- 📉 Historical Backtesting
- 🚀 REST APIs
- ✅ Automated Testing
- 📚 Interactive Swagger Documentation

Built as a production-ready backend for algorithmic trading and AI-powered financial analysis.
""",
    version="1.0.0",
)

# Register API Routers
app.include_router(market_router)
app.include_router(overview_router)
app.include_router(scanner_router)
app.include_router(indicator_router)
app.include_router(strategy_router)
app.include_router(backtest_router)
app.include_router(paper_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Trading OS 🚀",
        "version": "1.0.0",
        "docs": "/docs",
    }


@app.get("/health")
def health():
    return {
        "status": "running",
        "version": "1.0.0",
    }