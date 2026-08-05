from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_backtest_endpoint():
    response = client.get(
        "/backtest/BTCUSDT"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["symbol"] == "BTCUSDT"
    assert data["strategy"] == "Momentum"

    assert "final_balance" in data
    assert "profit_percent" in data
    assert "win_rate" in data