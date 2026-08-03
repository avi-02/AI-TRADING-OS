from typing import NamedTuple

from app.models.candle import Candle
from app.services.market_service import get_candles


class MarketData(NamedTuple):
    candles: list[Candle]
    closes: list[float]


def load_market_data(
    symbol: str,
    interval: str = "1h",
    limit: int = 100,
) -> MarketData | None:
    """
    Fetch market candles and extract commonly used data.
    """

    candles = get_candles(
        symbol=symbol,
        interval=interval,
        limit=limit,
    )

    if candles is None:
        return None

    closes = [
        candle.close_price
        for candle in candles
    ]

    return MarketData(
        candles=candles,
        closes=closes,
    )