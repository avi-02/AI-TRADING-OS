import pytest

from app.models.market import MarketTicker
from tests.fixtures.market_data import BINANCE_BTC_RESPONSE


@pytest.fixture
def sample_binance_response():
    return BINANCE_BTC_RESPONSE


@pytest.fixture
def sample_market_ticker():
    return MarketTicker(
        symbol="BTCUSDT",
        last_price=64000.0,
        open_price=63000.0,
        high_price=64500.0,
        low_price=62000.0,
        volume=1000.0,
        quote_volume=64000000.0,
        change_percent=2.5,
        trade_count=12345,
    )