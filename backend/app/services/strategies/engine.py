from app.models.strategy import StrategyResult
from app.services.strategies.momentum import momentum_strategy


def evaluate_strategy(
    symbol: str,
) -> StrategyResult:
    """
    Evaluate all available trading strategies.

    Currently only the Momentum Strategy is implemented.
    """

    return momentum_strategy(symbol)