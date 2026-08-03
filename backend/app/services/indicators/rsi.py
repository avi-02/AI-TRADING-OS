from app.models.indicator import RSIValue
from app.services.indicators.utils import load_market_data


def get_rsi(
    symbol: str,
    interval: str = "1h",
    period: int = 14,
    limit: int = 100,
) -> list[RSIValue] | None:
    """
    Calculate the Relative Strength Index (RSI)
    using Wilder's smoothing method.
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

    if len(closes) <= period:
        return []

    changes = [
        closes[i] - closes[i - 1]
        for i in range(1, len(closes))
    ]

    gains = [
        max(change, 0)
        for change in changes
    ]

    losses = [
        abs(min(change, 0))
        for change in changes
    ]

    avg_gain = sum(gains[:period]) / period
    avg_loss = sum(losses[:period]) / period

    rsi_values: list[RSIValue] = []

    if avg_loss == 0:
        first_rsi = 100.0
    else:
        rs = avg_gain / avg_loss
        first_rsi = 100 - (100 / (1 + rs))

    rsi_values.append(
        RSIValue(
            timestamp=candles[period].close_time,
            value=round(first_rsi, 2),
        )
    )

    for index in range(period, len(gains)):
        avg_gain = (
            (avg_gain * (period - 1))
            + gains[index]
        ) / period

        avg_loss = (
            (avg_loss * (period - 1))
            + losses[index]
        ) / period

        if avg_loss == 0:
            rsi = 100.0
        else:
            rs = avg_gain / avg_loss
            rsi = 100 - (100 / (1 + rs))

        rsi_values.append(
            RSIValue(
                timestamp=candles[index + 1].close_time,
                value=round(rsi, 2),
            )
        )

    return rsi_values