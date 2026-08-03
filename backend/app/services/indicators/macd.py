from app.models.indicator import MACDValue
from app.services.indicators.calculations import (
    calculate_ema,
    calculate_ema_from_series,
)
from app.services.indicators.utils import load_market_data


def get_macd(
    symbol: str,
    interval: str = "1h",
    limit: int = 100,
) -> list[MACDValue] | None:
    """
    Calculate MACD using:
    - EMA(12)
    - EMA(26)
    - Signal EMA(9)
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

    ema12 = calculate_ema(closes, 12)
    ema26 = calculate_ema(closes, 26)

    macd_line = []

    for fast, slow in zip(ema12, ema26):
        if fast is None or slow is None:
            macd_line.append(None)
        else:
            macd_line.append(fast - slow)

    signal_line = calculate_ema_from_series(
        macd_line,
        9,
    )

    macd_values: list[MACDValue] = []

    for candle, macd, signal in zip(
        candles,
        macd_line,
        signal_line,
    ):
        if macd is None or signal is None:
            continue

        histogram = macd - signal

        macd_values.append(
            MACDValue(
                timestamp=candle.close_time,
                macd=round(macd, 4),
                signal=round(signal, 4),
                histogram=round(histogram, 4),
            )
        )

    return macd_values