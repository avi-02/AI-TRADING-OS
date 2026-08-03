from app.models.indicator import SMAValue
from app.services.indicators.calculations import calculate_sma
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

    sma = calculate_sma(
        closes,
        period,
    )

    if not sma:
        return []

    sma_values: list[SMAValue] = []

    for candle, value in zip(candles, sma):
        if value is None:
            continue

        sma_values.append(
            SMAValue(
                timestamp=candle.close_time,
                value=round(value, 4),
            )
        )

    return sma_values