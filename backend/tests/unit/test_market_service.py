from app.models.market import MarketTicker
from app.services import market_service


def test_get_price_returns_market_price(
    mocker,
    sample_binance_response,
):
    mocker.patch(
        "app.services.market_service.fetch_price",
        return_value=sample_binance_response,
    )

    result = market_service.get_price("BTCUSDT")

    assert isinstance(result, MarketTicker)
    assert result.symbol == "BTCUSDT"
    assert result.last_price == 64000.0


def test_invalid_symbol_returns_none(mocker):
    mocker.patch(
        "app.services.market_service.fetch_price",
        return_value=None,
    )

    assert market_service.get_price("INVALID") is None