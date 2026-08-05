from app.models.strategy import Signal


def evaluate_momentum_signal(
    rsi_value: float,
    macd_histogram: float,
) -> tuple[Signal, int, list[str]]:
    """
    Evaluate the momentum trading signal using RSI and MACD.
    """

    reasons: list[str] = []

    if rsi_value < 40 and macd_histogram > 0:
        reasons.append(
            "RSI indicates bullish momentum."
        )
        reasons.append(
            "MACD histogram is positive."
        )

        return (
            Signal.BUY,
            80,
            reasons,
        )

    if rsi_value > 60 and macd_histogram < 0:
        reasons.append(
            "RSI indicates bearish momentum."
        )
        reasons.append(
            "MACD histogram is negative."
        )

        return (
            Signal.SELL,
            80,
            reasons,
        )

    return (
        Signal.HOLD,
        50,
        [
            "No strong momentum signal detected."
        ],
    )