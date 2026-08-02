from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_price(mocker, sample_market_ticker):
    mocker.patch(
        "app.api.market.get_price",
        return_value=sample_market_ticker,
    )

    response = client.get("/price/BTCUSDT")

    assert response.status_code == 200

    data = response.json()

    assert data["symbol"] == "BTCUSDT"
    assert data["last_price"] == 64000.0