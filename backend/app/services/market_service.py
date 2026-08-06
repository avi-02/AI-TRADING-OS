from datetime import UTC, datetime

from app.core.constants import DEFAULT_SYMBOLS
from app.models.candle import Candle
from app.models.market import MarketTicker
from app.repositories import market_repository


def get_price(symbol: str) -> MarketTicker | None:
    """
    Fetch and transform market data for a trading symbol.
    """
    data = market_repository.fetch_price(symbol)

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


def get_candles(
    symbol: str,
    interval: str = "1h",
    limit: int = 100,
) -> list[Candle] | None:
    """
    Fetch and transform historical candle data.
    """

    data = market_repository.fetch_candles(
        symbol=symbol,
        interval=interval,
        limit=limit,
    )

    if data is None:
        return None

    candles: list[Candle] = []

    for candle in data:
        candles.append(
            Candle(
                open_time=datetime.fromtimestamp(
                    candle[0] / 1000,
                    tz=UTC,
                ),
                close_time=datetime.fromtimestamp(
                    candle[6] / 1000,
                    tz=UTC,
                ),
                open_price=float(candle[1]),
                high_price=float(candle[2]),
                low_price=float(candle[3]),
                close_price=float(candle[4]),
                volume=float(candle[5]),
                quote_volume=float(candle[7]),
                trade_count=int(candle[8]),
                taker_buy_base_volume=float(candle[9]),
                taker_buy_quote_volume=float(candle[10]),
            )
        )

    return candles