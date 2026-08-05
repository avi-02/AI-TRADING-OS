from app.services.backtesting.engine import run_backtest


def test_run_backtest():
    """
    Verify the backtest engine returns a valid result.
    """

    result = run_backtest("BTCUSDT")

    assert result is not None
    assert result.symbol == "BTCUSDT"
    assert result.strategy == "Momentum"

    assert result.initial_balance > 0
    assert result.final_balance > 0

    assert result.total_trades >= 0
    assert result.winning_trades >= 0
    assert result.losing_trades >= 0

    assert 0 <= result.win_rate <= 100