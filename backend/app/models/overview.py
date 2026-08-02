from pydantic import BaseModel

from app.models.market import MarketTicker


class MarketOverview(BaseModel):
    """
    Represents a high-level overview of the tracked crypto market.
    """

    watchlist_size: int

    highest_price: MarketTicker

    highest_volume: MarketTicker

    top_gainer: MarketTicker

    top_loser: MarketTicker | None = None