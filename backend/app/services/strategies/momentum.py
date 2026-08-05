from app.models.strategy import (
    Signal,
    StrategyResult,
)

from app.services.indicators import (
    get_macd,
    get_rsi,
)


def momentum_strategy(
    symbol: str,
) -> StrategyResult:
    """
    Momentum Strategy using RSI and MACD.
    """

    rsi = get_rsi(symbol)
    macd = get_macd(symbol)

    if not rsi or not macd:
        return StrategyResult(
            symbol=symbol,
            signal=Signal.HOLD,
            confidence=0,
            reasons=[
                "Unable to calculate indicators.",
            ],
        )

    latest_rsi = rsi[-1]
    latest_macd = macd[-1]

    reasons: list[str] = []

    # BUY Signal
    if (
        latest_rsi.value < 30
        and latest_macd.histogram > 0
    ):
        reasons.append(
            "RSI indicates oversold conditions."
        )
        reasons.append(
            "MACD histogram is bullish."
        )

        return StrategyResult(
            symbol=symbol,
            signal=Signal.BUY,
            confidence=80,
            reasons=reasons,
        )

    # SELL Signal
    if (
        latest_rsi.value > 70
        and latest_macd.histogram < 0
    ):
        reasons.append(
            "RSI indicates overbought conditions."
        )
        reasons.append(
            "MACD histogram is bearish."
        )

        return StrategyResult(
            symbol=symbol,
            signal=Signal.SELL,
            confidence=80,
            reasons=reasons,
        )

    # HOLD Signal
    reasons.append(
        "No strong momentum signal detected."
    )

    return StrategyResult(
        symbol=symbol,
        signal=Signal.HOLD,
        confidence=50,
        reasons=reasons,
    )