from app.models.indicator import BollingerBandValue
from app.services.indicators.calculations import (
    calculate_sma,
    calculate_standard_deviation,
)
from app.services.indicators.utils import load_market_data


def get_bollinger_bands(
    symbol: str,
    interval: str = "1h",
    period: int = 20,
    limit: int = 100,
    multiplier: float = 2.0,
) -> list[BollingerBandValue] | None:
    """
    Calculate Bollinger Bands.
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

    std = calculate_standard_deviation(
        closes,
        period,
    )

    bands: list[BollingerBandValue] = []

    for candle, middle, deviation in zip(
        candles,
        sma,
        std,
    ):
        if middle is None or deviation is None:
            continue

        upper = middle + (multiplier * deviation)
        lower = middle - (multiplier * deviation)

        bands.append(
            BollingerBandValue(
                timestamp=candle.close_time,
                upper_band=round(upper, 4),
                middle_band=round(middle, 4),
                lower_band=round(lower, 4),
            )
        )

    return bands