from unittest.mock import patch

from app.models.market import MarketTicker
from app.services.paper_trading.orders import OrderService
from app.services.paper_trading.portfolio import portfolio_service


@patch("app.services.paper_trading.orders.get_price")
def test_buy_order(mock_get_price):
    """
    Verify a BUY order updates the portfolio.
    """

    mock_get_price.return_value = MarketTicker(
        symbol="BTCUSDT",
        last_price=50000,
        open_price=49000,
        high_price=51000,
        low_price=48000,
        volume=1000,
        quote_volume=50000000,
        change_percent=2.5,
        trade_count=100,
    )

    portfolio_service.reset(10000)

    service = OrderService()

    result = service.buy(
        "BTCUSDT",
        1000,
    )

    assert result.status == "FILLED"
    assert result.side == "BUY"

    portfolio = portfolio_service.get_portfolio()

    assert portfolio.cash == 9000
    assert len(portfolio.positions) == 1


@patch("app.services.paper_trading.orders.get_price")
def test_sell_order(mock_get_price):
    """
    Verify a SELL order closes the position.
    """

    mock_get_price.return_value = MarketTicker(
        symbol="BTCUSDT",
        last_price=50000,
        open_price=49000,
        high_price=51000,
        low_price=48000,
        volume=1000,
        quote_volume=50000000,
        change_percent=2.5,
        trade_count=100,
    )

    portfolio_service.reset(10000)

    service = OrderService()

    service.buy(
        "BTCUSDT",
        1000,
    )

    result = service.sell(
        "BTCUSDT"
    )

    assert result.status == "FILLED"
    assert result.side == "SELL"

    portfolio = portfolio_service.get_portfolio()

    assert portfolio.cash == 10000
    assert portfolio.positions == []