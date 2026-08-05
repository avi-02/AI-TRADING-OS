from fastapi import APIRouter, HTTPException
from app.models.auto_trade import AutoTradeResult
from app.services.paper_trading.auto import auto_trade_service

from app.models.pnl import PortfolioSummary
from app.models.portfolio import (
    OrderRequest,
    OrderResponse,
    Portfolio,
)

from app.services.paper_trading.orders import order_service
from app.services.paper_trading.pnl import pnl_service
from app.services.paper_trading.portfolio import (
    portfolio_service,
)

router = APIRouter(
    prefix="/paper",
    tags=["Paper Trading"],
)


@router.get(
    "/portfolio",
    response_model=Portfolio,
)
def get_portfolio():
    """
    Get the current paper trading portfolio.
    """
    return portfolio_service.get_portfolio()


@router.get(
    "/pnl",
    response_model=PortfolioSummary,
)
def get_pnl():
    """
    Get the current portfolio performance.
    """
    return pnl_service.get_summary()


@router.post(
    "/buy/{symbol}",
    response_model=OrderResponse,
)
def buy(
    symbol: str,
    request: OrderRequest,
):
    """
    Execute a paper BUY order.
    """

    try:
        return order_service.buy(
            symbol=symbol.upper(),
            amount=request.amount,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )


@router.post(
    "/sell/{symbol}",
    response_model=OrderResponse,
)
def sell(
    symbol: str,
):
    """
    Sell the entire paper position.
    """

    try:
        return order_service.sell(
            symbol.upper(),
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )


@router.post(
    "/reset",
    response_model=Portfolio,
)
def reset():
    """
    Reset the paper trading portfolio.
    """

    return portfolio_service.reset()

@router.post(
    "/auto/{symbol}",
    response_model=AutoTradeResult,
)
def auto_trade(
    symbol: str,
):
    """
    Execute the trading strategy and automatically
    place a paper trade if a BUY or SELL signal occurs.
    """

    return auto_trade_service.execute(
        symbol.upper(),
    )