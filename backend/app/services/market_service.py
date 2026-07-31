from app.core.constants import DEFAULT_SYMBOLS
from app.models.market import MarketTicker
from app.repositories.market_repository import fetch_price


def get_price(symbol: str) -> MarketTicker | None:
    """
    Fetch and transform market data for a trading symbol.
    """
    data = fetch_price(symbol)

    if data is None:
        return None

    return MarketTicker(
        symbol=data["symbol"],
        last_price=float(data["lastPrice"]),
        open_price=float(data["openPrice"]),
        high_price=float(data["highPrice"]),
        low_price=float(data["lowPrice"]),
        volume=float(data["volume"]),
        quote_volume=float(data["quoteVolume"]),
        change_percent=float(data["priceChangePercent"]),
        trade_count=int(data["count"]),
    )


def get_multiple_prices() -> list[MarketTicker]:
    """
    Fetch market data for the default watchlist.
    """
    prices: list[MarketTicker] = []

    for symbol in DEFAULT_SYMBOLS:
        market = get_price(symbol)

        if market is not None:
            prices.append(market)

    return prices