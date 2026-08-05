from unittest.mock import patch

from app.models.backtest import BacktestResult
from app.services.backtesting.engine import run_backtest


@patch("app.services.backtesting.engine.calculate_metrics")
@patch("app.services.backtesting.engine.simulate_trades")
@patch("app.services.backtesting.engine.generate_momentum_signals")
@patch("app.services.backtesting.engine.get_macd")
@patch("app.services.backtesting.engine.get_rsi")
@patch("app.services.backtesting.engine.get_candles")
def test_run_backtest(
    mock_get_candles,
    mock_get_rsi,
    mock_get_macd,
    mock_generate_signals,
    mock_simulator,
    mock_metrics,
):
    class Candle:
        def __init__(self, close_price):
            self.close_price = close_price

    mock_get_candles.return_value = [
        Candle(100),
        Candle(105),
        Candle(110),
    ]

    mock_get_rsi.return_value = [object(), object(), object()]
    mock_get_macd.return_value = [object(), object(), object()]
    mock_generate_signals.return_value = ["BUY", "HOLD", "SELL"]

    mock_simulator.return_value = (
        11000,
        1,
        1,
        0,
    )

    mock_metrics.return_value = {
        "profit_percent": 10,
        "total_trades": 1,
        "winning_trades": 1,
        "losing_trades": 0,
        "win_rate": 100,
    }

    result = run_backtest("BTCUSDT")

    assert isinstance(result, BacktestResult)
    assert result.symbol == "BTCUSDT"
    assert result.strategy == "Momentum"
    assert result.final_balance == 11000