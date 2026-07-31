from app.models.market import MarketTicker
from app.services.market_service import get_price


def test_get_price_returns_market_price():
    result = get_price("BTCUSDT")

    assert result is not None
    assert isinstance(result, MarketTicker)
    assert result.symbol == "BTCUSDT"
    assert result.last_price > 0

def test_invalid_symbol_returns_none():
    result = get_price("INVALIDCOIN")

    assert result is None