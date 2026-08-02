from fastapi.testclient import TestClient

from app.main import app
from app.models.market import MarketTicker

client = TestClient(app)


sample_response = [
    MarketTicker(
        symbol="SOLUSDT",
        last_price=150,
        open_price=140,
        high_price=160,
        low_price=130,
        volume=200,
        quote_volume=8000000,
        change_percent=5.0,
        trade_count=2000,
    ),
    MarketTicker(
        symbol="BTCUSDT",
        last_price=60000,
        open_price=59000,
        high_price=61000,
        low_price=58000,
        volume=100,
        quote_volume=6000000,
        change_percent=2.5,
        trade_count=1000,
    ),
]


def test_scanner_gainers_api(mocker):
    mocker.patch(
        "app.api.scanner.get_top_gainers",
        return_value=sample_response,
    )

    response = client.get("/scanner/gainers")

    assert response.status_code == 200
    assert response.json()[0]["symbol"] == "SOLUSDT"


def test_scanner_losers_api(mocker):
    mocker.patch(
        "app.api.scanner.get_top_losers",
        return_value=sample_response,
    )

    response = client.get("/scanner/losers")

    assert response.status_code == 200


def test_scanner_high_volume_api(mocker):
    mocker.patch(
        "app.api.scanner.get_high_volume",
        return_value=sample_response,
    )

    response = client.get("/scanner/high-volume")

    assert response.status_code == 200


def test_scanner_most_active_api(mocker):
    mocker.patch(
        "app.api.scanner.get_most_active",
        return_value=sample_response,
    )

    response = client.get("/scanner/most-active")

    assert response.status_code == 200