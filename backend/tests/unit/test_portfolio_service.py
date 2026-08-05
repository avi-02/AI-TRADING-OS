from app.services.paper_trading.portfolio import (
    PortfolioService,
)


def test_portfolio_reset():
    """
    Verify portfolio reset restores the initial cash balance.
    """

    service = PortfolioService()

    portfolio = service.reset(5000)

    assert portfolio.cash == 5000
    assert portfolio.positions == []


def test_get_empty_portfolio():
    """
    Verify a new portfolio starts empty.
    """

    service = PortfolioService()

    portfolio = service.get_portfolio()

    assert portfolio.cash == 10000
    assert portfolio.positions == []


def test_get_position():
    """
    Verify get_position returns None
    when no position exists.
    """

    service = PortfolioService()

    assert service.get_position("BTCUSDT") is None