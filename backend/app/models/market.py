from pydantic import BaseModel


class MarketTicker(BaseModel):
    symbol: str
    last_price: float
    open_price: float
    high_price: float
    low_price: float
    volume: float
    quote_volume: float
    change_percent: float
    trade_count: int