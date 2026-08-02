from app.models.market import MarketTicker
from app.services import scanner_service


def sample_market_data():
    return [
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
    ]


def test_get_top_gainers(mocker):
    mocker.patch(
        "app.services.scanner_service.get_multiple_prices",
        return_value=sample_market_data(),
    )

    result = scanner_service.get_top_gainers(limit=2)

    assert len(result) == 2
    assert result[0].symbol == "SOLUSDT"
    assert result[1].symbol == "BTCUSDT"


def test_get_top_losers(mocker):
    mocker.patch(
        "app.services.scanner_service.get_multiple_prices",
        return_value=sample_market_data(),
    )

    result = scanner_service.get_top_losers(limit=1)

    assert len(result) == 1
    assert result[0].symbol == "ETHUSDT"


def test_get_high_volume(mocker):
    mocker.patch(
        "app.services.scanner_service.get_multiple_prices",
        return_value=sample_market_data(),
    )

    result = scanner_service.get_high_volume(limit=1)

    assert result[0].symbol == "SOLUSDT"


def test_get_most_active(mocker):
    mocker.patch(
        "app.services.scanner_service.get_multiple_prices",
        return_value=sample_market_data(),
    )

    result = scanner_service.get_most_active(limit=1)

    assert result[0].symbol == "SOLUSDT"