from app.models.market import MarketTicker
from app.services import overview_service


def test_market_overview_with_loser(mocker):
    sample_data = [
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
        MarketTicker(
            symbol="ETHUSDT",
            last_price=3000,
            open_price=3100,
            high_price=3200,
            low_price=2900,
            volume=500,
            quote_volume=1500000,
            change_percent=-1.2,
            trade_count=500,
        ),
    ]

    mocker.patch(
        "app.services.overview_service.get_multiple_prices",
        return_value=sample_data,
    )

    overview = overview_service.get_market_overview()

    assert overview.watchlist_size == 2
    assert overview.highest_price.symbol == "BTCUSDT"
    assert overview.highest_volume.symbol == "BTCUSDT"
    assert overview.top_gainer.symbol == "BTCUSDT"

    assert overview.top_loser is not None
    assert overview.top_loser.symbol == "ETHUSDT"


def test_market_overview_without_loser(mocker):
    sample_data = [
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
        MarketTicker(
            symbol="ETHUSDT",
            last_price=3000,
            open_price=2900,
            high_price=3100,
            low_price=2800,
            volume=500,
            quote_volume=1500000,
            change_percent=1.5,
            trade_count=500,
        ),
    ]

    mocker.patch(
        "app.services.overview_service.get_multiple_prices",
        return_value=sample_data,
    )

    overview = overview_service.get_market_overview()

    assert overview.watchlist_size == 2
    assert overview.top_loser is None