from app.models.strategy import (
    Signal,
    StrategyResult,
)

from app.services.indicators import (
    get_macd,
    get_rsi,
)

from app.services.strategies.utils import (
    evaluate_momentum_signal,
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

    signal, confidence, reasons = evaluate_momentum_signal(
        latest_rsi.value,
        latest_macd.histogram,
    )

    return StrategyResult(
        symbol=symbol,
        signal=signal,
        confidence=confidence,
        reasons=reasons,
    )