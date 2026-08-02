from fastapi.testclient import TestClient

from app.main import app
from app.models.market import MarketTicker
from app.models.overview import MarketOverview

client = TestClient(app)


def test_market_overview_api(mocker):
    overview = MarketOverview(
        watchlist_size=1,
        highest_price=MarketTicker(
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
        highest_volume=MarketTicker(
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
        top_gainer=MarketTicker(
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
        top_loser=None,
    )

    mocker.patch(
        "app.api.overview.get_market_overview",
        return_value=overview,
    )

    response = client.get("/market/overview")

    assert response.status_code == 200

    data = response.json()

    assert data["watchlist_size"] == 1
    assert data["highest_price"]["symbol"] == "BTCUSDT"
    assert data["highest_volume"]["symbol"] == "BTCUSDT"
    assert data["top_gainer"]["symbol"] == "BTCUSDT"
    assert data["top_loser"] is None