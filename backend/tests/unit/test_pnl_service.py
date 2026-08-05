from unittest.mock import patch

from app.models.market import MarketTicker
from app.services.paper_trading.orders import order_service
from app.services.paper_trading.pnl import PnLService
from app.services.paper_trading.portfolio import portfolio_service


@patch("app.services.paper_trading.pnl.get_price")
@patch("app.services.paper_trading.orders.get_price")
def test_portfolio_summary(
    mock_order_price,
    mock_pnl_price,
):
    """
    Verify portfolio summary calculations.
    """

    ticker = MarketTicker(
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

    mock_order_price.return_value = ticker
    mock_pnl_price.return_value = ticker

    portfolio_service.reset(10000)

    order_service.buy(
        "BTCUSDT",
        1000,
    )

    service = PnLService()

    summary = service.get_summary()

    assert summary.cash == 9000
    assert summary.market_value == 1000
    assert summary.portfolio_value == 10000
    assert summary.profit == 0
    assert summary.total_positions == 1