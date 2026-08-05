from app.models.backtest import BacktestResult

from app.services.market_service import get_candles
from app.services.indicators import (
    get_macd,
    get_rsi,
)
from app.services.strategies.history import (
    generate_momentum_signals,
)

from .metrics import calculate_metrics
from .simulator import simulate_trades


def run_backtest(
    symbol: str,
    interval: str = "1h",
    limit: int = 100,
    initial_balance: float = 10_000,
) -> BacktestResult | None:
    """
    Run a momentum strategy backtest.
    """

    candles = get_candles(
        symbol=symbol,
        interval=interval,
        limit=limit,
    )

    # No candle data available
    if not candles:
        return None

    rsi = get_rsi(
        symbol=symbol,
        interval=interval,
        limit=limit,
    )

    macd = get_macd(
        symbol=symbol,
        interval=interval,
        limit=limit,
    )

    # Ensure all indicator data is available
    if not rsi or not macd:
        return None

    # Ensure all series have matching lengths
    if (
        len(candles) != len(rsi)
        or len(candles) != len(macd)
    ):
        return None

    signals = generate_momentum_signals(
        rsi,
        macd,
    )

    prices = [
        candle.close_price
        for candle in candles
    ]

    final_balance, total_trades, winning_trades, losing_trades = simulate_trades(
        prices=prices,
        signals=signals,
        initial_balance=initial_balance,
    )

    metrics = calculate_metrics(
        initial_balance=initial_balance,
        final_balance=final_balance,
        total_trades=total_trades,
        winning_trades=winning_trades,
        losing_trades=losing_trades,
    )

    return BacktestResult(
        symbol=symbol,
        strategy="Momentum",
        initial_balance=initial_balance,
        final_balance=final_balance,
        profit_percent=metrics["profit_percent"],
        total_trades=metrics["total_trades"],
        winning_trades=metrics["winning_trades"],
        losing_trades=metrics["losing_trades"],
        win_rate=metrics["win_rate"],
    )