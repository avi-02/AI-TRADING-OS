from typing import List

from fastapi import APIRouter, HTTPException, Query

from app.models.candle import Candle
from app.models.market import MarketTicker
from app.services.market_service import (
    get_candles,
    get_multiple_prices,
    get_price,
)

router = APIRouter()


@router.get(
    "/price/{symbol}",
    response_model=MarketTicker,
)
def price(symbol: str):
    data = get_price(symbol.upper())

    if data is None:
        raise HTTPException(
            status_code=404,
            detail=f"Invalid Trading Symbol: {symbol}",
        )

    return data


@router.get(
    "/prices",
    response_model=List[MarketTicker],
)
def prices():
    return get_multiple_prices()


@router.get(
    "/candles/{symbol}",
    response_model=List[Candle],
)
def candles(
    symbol: str,
    interval: str = Query(
        default="1h",
        description="Candle interval (1m, 5m, 15m, 1h, 4h, 1d)",
    ),
    limit: int = Query(
        default=100,
        ge=1,
        le=1000,
        description="Number of candles",
    ),
):
    """
    Return historical OHLCV candle data.
    """

    data = get_candles(
        symbol=symbol.upper(),
        interval=interval,
        limit=limit,
    )

    if data is None:
        raise HTTPException(
            status_code=404,
            detail=f"Unable to fetch candles for {symbol}",
        )

    return data