from typing import Optional


def calculate_sma(
    values: list[float],
    period: int,
) -> list[Optional[float]]:
    """
    Calculate Simple Moving Average.

    Returns a list aligned with the input values.
    Entries before the first complete window are None.
    """

    if len(values) < period:
        return []

    sma: list[Optional[float]] = [None] * (period - 1)

    for index in range(period - 1, len(values)):
        window = values[index - period + 1:index + 1]
        sma.append(sum(window) / period)

    return sma


def calculate_ema(
    values: list[float],
    period: int,
) -> list[Optional[float]]:
    """
    Calculate Exponential Moving Average.

    Returns a list aligned with the input values.
    Entries before the first EMA are None.
    """

    if len(values) < period:
        return []

    ema: list[Optional[float]] = [None] * (period - 1)

    first = sum(values[:period]) / period
    ema.append(first)

    multiplier = 2 / (period + 1)

    previous = first

    for price in values[period:]:
        previous = ((price - previous) * multiplier) + previous
        ema.append(previous)

    return ema 

def calculate_ema_from_series(
    values: list[Optional[float]],
    period: int,
) -> list[Optional[float]]:
    """
    Calculate EMA from a series that may contain leading None values.
    """

    first_valid = next(
        (i for i, value in enumerate(values) if value is not None),
        None,
    )

    if first_valid is None:
        return []

    valid_values = [v for v in values if v is not None]

    ema = calculate_ema(valid_values, period)

    result: list[Optional[float]] = [None] * first_valid
    result.extend(ema)

    return result