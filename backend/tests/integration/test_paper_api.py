from unittest.mock import patch

from fastapi.testclient import TestClient

from app.main import app
from app.models.auto_trade import AutoTradeResult
from app.models.pnl import PortfolioSummary
from app.models.portfolio import (
    OrderResponse,
    Portfolio,
)
from app.models.strategy import (
    Signal,
    StrategyResult,
)

client = TestClient(app)


@patch("app.api.paper.portfolio_service")
def test_get_portfolio(mock_service):
    mock_service.get_portfolio.return_value = Portfolio(
        cash=10000,
        positions=[],
    )

    response = client.get("/paper/portfolio")

    assert response.status_code == 200
    assert response.json()["cash"] == 10000


@patch("app.api.paper.pnl_service")
def test_get_pnl(mock_service):
    mock_service.get_summary.return_value = PortfolioSummary(
        cash=10000,
        market_value=0,
        portfolio_value=10000,
        profit=0,
        profit_percent=0,
        total_positions=0,
    )

    response = client.get("/paper/pnl")

    assert response.status_code == 200
    assert response.json()["portfolio_value"] == 10000


@patch("app.api.paper.order_service")
def test_buy(mock_service):
    mock_service.buy.return_value = OrderResponse(
        symbol="BTCUSDT",
        side="BUY",
        price=50000,
        quantity=0.02,
        remaining_cash=9000,
        status="FILLED",
    )

    response = client.post(
        "/paper/buy/BTCUSDT",
        json={"amount": 1000},
    )

    assert response.status_code == 200
    assert response.json()["side"] == "BUY"


@patch("app.api.paper.order_service")
def test_sell(mock_service):
    mock_service.sell.return_value = OrderResponse(
        symbol="BTCUSDT",
        side="SELL",
        price=50000,
        quantity=0.02,
        remaining_cash=10000,
        status="FILLED",
    )

    response = client.post("/paper/sell/BTCUSDT")

    assert response.status_code == 200
    assert response.json()["side"] == "SELL"


@patch("app.api.paper.auto_trade_service")
def test_auto_trade(mock_service):
    mock_service.execute.return_value = AutoTradeResult(
        strategy=StrategyResult(
            symbol="BTCUSDT",
            signal=Signal.HOLD,
            confidence=50,
            reasons=["No signal"],
        ),
        order=None,
    )

    response = client.post("/paper/auto/BTCUSDT")

    assert response.status_code == 200
    assert response.json()["strategy"]["signal"] == "HOLD"


@patch("app.api.paper.portfolio_service")
def test_reset(mock_service):
    mock_service.reset.return_value = Portfolio(
        cash=10000,
        positions=[],
    )

    response = client.post("/paper/reset")

    assert response.status_code == 200
    assert response.json()["cash"] == 10000