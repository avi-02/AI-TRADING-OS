from unittest.mock import patch

from fastapi.testclient import TestClient

from app.main import app
from app.models.backtest import BacktestResult

client = TestClient(app)


@patch("app.api.backtest.run_backtest")
def test_backtest_endpoint(mock_backtest):

    mock_backtest.return_value = BacktestResult(
        symbol="BTCUSDT",
        strategy="Momentum",
        initial_balance=10000,
        final_balance=11000,
        profit_percent=10,
        total_trades=1,
        winning_trades=1,
        losing_trades=0,
        win_rate=100,
    )

    response = client.get("/backtest/BTCUSDT")

    assert response.status_code == 200

    data = response.json()

    assert data["symbol"] == "BTCUSDT"
    assert data["strategy"] == "Momentum"
    assert data["profit_percent"] == 10