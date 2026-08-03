from typing import List

from fastapi import APIRouter, HTTPException, Query

from app.models.indicator import EMAValue, SMAValue,RSIValue
from app.services.indicators import get_ema, get_sma,get_rsi

router = APIRouter(
    prefix="/indicator",
    tags=["Technical Indicators"],
)


@router.get(
    "/sma/{symbol}",
    response_model=List[SMAValue],
)
def sma(
    symbol: str,
    interval: str = Query(
        default="1h",
        description="Candle interval",
    ),
    period: int = Query(
        default=20,
        ge=2,
        le=200,
        description="Moving average period",
    ),
    limit: int = Query(
        default=100,
        ge=20,
        le=1000,
        description="Number of candles",
    ),
):
    """
    Calculate the Simple Moving Average (SMA).
    """

    result = get_sma(
        symbol=symbol.upper(),
        interval=interval,
        period=period,
        limit=limit,
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail=f"Unable to calculate SMA for {symbol}",
        )

    return result


@router.get(
    "/ema/{symbol}",
    response_model=List[EMAValue],
)
def ema(
    symbol: str,
    interval: str = Query(
        default="1h",
        description="Candle interval",
    ),
    period: int = Query(
        default=20,
        ge=2,
        le=200,
        description="EMA period",
    ),
    limit: int = Query(
        default=100,
        ge=20,
        le=1000,
        description="Number of candles",
    ),
):
    """
    Calculate the Exponential Moving Average (EMA).
    """

    result = get_ema(
        symbol=symbol.upper(),
        interval=interval,
        period=period,
        limit=limit,
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail=f"Unable to calculate EMA for {symbol}",
        )

    return result 

@router.get(
    "/rsi/{symbol}",
    response_model=list[RSIValue],
)
def rsi(
    symbol: str,
    interval: str = Query(
        default="1h",
        description="Candle interval",
    ),
    period: int = Query(
        default=14,
        ge=2,
        le=200,
        description="RSI period",
    ),
    limit: int = Query(
        default=100,
        ge=20,
        le=1000,
        description="Number of candles",
    ),
):
    """
    Calculate the Relative Strength Index (RSI).
    """

    result = get_rsi(
        symbol=symbol.upper(),
        interval=interval,
        period=period,
        limit=limit,
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail=f"Unable to calculate RSI for {symbol}",
        )

    return result