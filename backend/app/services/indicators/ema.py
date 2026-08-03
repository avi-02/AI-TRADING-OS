from app.models.indicator import EMAValue
from app.services.indicators.utils import load_market_data


def get_ema(
    symbol: str,
    interval: str = "1h",
    period: int = 14,
    limit: int = 100,
) -> list[EMAValue] | None:
    """
    Calculate the Exponential Moving Average (EMA).
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

    multiplier = 2 / (period + 1)

    sma = sum(closes[:period]) / period
    ema = sma

    ema_values: list[EMAValue] = [
        EMAValue(
            timestamp=candles[period - 1].close_time,
            value=round(ema, 4),
        )
    ]

    for index in range(period, len(closes)):
        ema = ((closes[index] - ema) * multiplier) + ema

        ema_values.append(
            EMAValue(
                timestamp=candles[index].close_time,
                value=round(ema, 4),
            )
        )

    return ema_values