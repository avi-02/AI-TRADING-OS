from app.models.indicator import EMAValue
from app.services.indicators.calculations import calculate_ema
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

    ema = calculate_ema(
        closes,
        period,
    )

    if not ema:
        return []

    ema_values: list[EMAValue] = []

    for candle, value in zip(candles, ema):
        if value is None:
            continue

        ema_values.append(
            EMAValue(
                timestamp=candle.close_time,
                value=round(value, 4),
            )
        )

    return ema_values