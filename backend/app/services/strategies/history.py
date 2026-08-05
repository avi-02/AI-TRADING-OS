from app.models.strategy import Signal

from app.services.strategies.utils import (
    evaluate_momentum_signal,
)


def generate_momentum_signals(
    rsi_values,
    macd_values,
) -> list[Signal]:
    """
    Generate trading signals for every candle.
    """

    signals: list[Signal] = []

    for rsi, macd in zip(
        rsi_values,
        macd_values,
    ):
        signal, _, _ = evaluate_momentum_signal(
            rsi.value,
            macd.histogram,
        )

        signals.append(signal)

    return signals