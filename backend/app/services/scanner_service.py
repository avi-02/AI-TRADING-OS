from collections.abc import Callable

from app.models.market import MarketTicker
from app.services.market_service import get_multiple_prices


def _rank_market_data(
    *,
    key_func: Callable[[MarketTicker], float | int],
    reverse: bool = True,
    limit: int = 5,
) -> list[MarketTicker]:
    """
    Generic ranking helper used by all scanner endpoints.
    """

    market_data = get_multiple_prices()

    return sorted(
        market_data,
        key=key_func,
        reverse=reverse,
    )[:limit]


def get_top_gainers(limit: int = 5) -> list[MarketTicker]:
    """
    Return the top gaining assets.
    """
    return _rank_market_data(
        key_func=lambda coin: coin.change_percent,
        reverse=True,
        limit=limit,
    )


def get_top_losers(limit: int = 5) -> list[MarketTicker]:
    """
    Return the top losing assets.
    """
    return _rank_market_data(
        key_func=lambda coin: coin.change_percent,
        reverse=False,
        limit=limit,
    )


def get_high_volume(limit: int = 5) -> list[MarketTicker]:
    """
    Return assets ranked by quote volume.
    """
    return _rank_market_data(
        key_func=lambda coin: coin.quote_volume,
        reverse=True,
        limit=limit,
    )


def get_most_active(limit: int = 5) -> list[MarketTicker]:
    """
    Return assets ranked by trade count.
    """
    return _rank_market_data(
        key_func=lambda coin: coin.trade_count,
        reverse=True,
        limit=limit,
    )