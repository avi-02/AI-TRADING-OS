def calculate_metrics(
    initial_balance: float,
    final_balance: float,
    total_trades: int,
    winning_trades: int,
    losing_trades: int,
) -> dict:
    """
    Calculate backtesting performance metrics.
    """

    profit_percent = (
        (final_balance - initial_balance)
        / initial_balance
    ) * 100

    if total_trades == 0:
        win_rate = 0.0
    else:
        win_rate = (
            winning_trades / total_trades
        ) * 100

    return {
        "profit_percent": round(
            profit_percent,
            2,
        ),
        "win_rate": round(
            win_rate,
            2,
        ),
        "total_trades": total_trades,
        "winning_trades": winning_trades,
        "losing_trades": losing_trades,
    }