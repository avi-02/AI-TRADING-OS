from app.models.indicator import SMAValue
from app.services.indicators.utils import load_market_data


def get_sma(
    symbol: str,
    interval: str = "1h",
    period: int = 14,
    limit: int = 100,
) -> list[SMAValue] | None:
    """
    Calculate the Simple Moving Average (SMA).
    """

    market_data = load_market_data(
        symbol=symbol,
        interval=interval,
        limit=limit,
    )

    if market_data is None:
        return None

    candles = market_data.candles
    closes = market_data.closes

    if len(closes) < period:
        return []

    sma_values: list[SMAValue] = []

    for index in range(period - 1, len(closes)):
        window = closes[index - period + 1 : index + 1]

        sma = sum(window) / period

        sma_values.append(
            SMAValue(
                timestamp=candles[index].close_time,
                value=round(sma, 4),
            )
        )

    return sma_values