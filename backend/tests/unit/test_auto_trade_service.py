from unittest.mock import patch

from app.models.portfolio import OrderResponse
from app.models.strategy import (
    Signal,
    StrategyResult,
)
from app.services.paper_trading.auto import (
    AutoTradeService,
)


@patch("app.services.paper_trading.auto.order_service.buy")
@patch("app.services.paper_trading.auto.evaluate_strategy")
def test_auto_buy(
    mock_strategy,
    mock_buy,
):
    """
    Verify BUY signals execute a paper BUY order.
    """

    mock_strategy.return_value = StrategyResult(
        symbol="BTCUSDT",
        signal=Signal.BUY,
        confidence=80,
        reasons=["BUY"],
    )

    mock_buy.return_value = OrderResponse(
        symbol="BTCUSDT",
        side="BUY",
        price=50000,
        quantity=0.02,
        remaining_cash=9000,
        status="FILLED",
    )

    service = AutoTradeService()

    result = service.execute("BTCUSDT")

    assert result.strategy.signal == Signal.BUY
    assert result.order is not None
    assert result.order.side == "BUY"


@patch("app.services.paper_trading.auto.evaluate_strategy")
def test_auto_hold(
    mock_strategy,
):
    """
    Verify HOLD signals do not execute orders.
    """

    mock_strategy.return_value = StrategyResult(
        symbol="BTCUSDT",
        signal=Signal.HOLD,
        confidence=50,
        reasons=["HOLD"],
    )

    service = AutoTradeService()

    result = service.execute("BTCUSDT")

    assert result.strategy.signal == Signal.HOLD
    assert result.order is None