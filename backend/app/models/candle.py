from datetime import datetime

from pydantic import BaseModel


class Candle(BaseModel):
    """
    Represents a single OHLCV candlestick.
    """

    open_time: datetime
    close_time: datetime

    open_price: float
    high_price: float
    low_price: float
    close_price: float

    volume: float
    quote_volume: float

    trade_count: int

    taker_buy_base_volume: float
    taker_buy_quote_volume: float