from typing import List

from fastapi import APIRouter, HTTPException

from app.models.market import MarketTicker
from app.services.market_service import (
    get_multiple_prices,
    get_price,
)

router = APIRouter()


@router.get(
    "/price/{symbol}",
    response_model=MarketTicker
)
def price(symbol: str):
    data = get_price(symbol.upper())

    if data is None:
        raise HTTPException(
            status_code=404,
            detail=f"Invalid trading symbol: {symbol}"
        )

    return data


@router.get(
    "/prices",
    response_model=List[MarketTicker]
)
def prices():
    return get_multiple_prices()