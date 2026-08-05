from fastapi import APIRouter, HTTPException, Query

from app.models.backtest import BacktestResult
from app.services.backtesting.engine import run_backtest

router = APIRouter(
    prefix="/backtest",
    tags=["Backtesting"],
)


@router.get(
    "/{symbol}",
    response_model=BacktestResult,
)
def backtest(
    symbol: str,
    interval: str = Query(
        default="1h",
        description="Candle interval",
    ),
    limit: int = Query(
        default=100,
        ge=50,
        le=1000,
        description="Number of historical candles",
    ),
    initial_balance: float = Query(
        default=10000,
        gt=0,
        description="Starting capital",
    ),
):
    """
    Run a historical backtest using the Momentum strategy.
    """

    result = run_backtest(
        symbol=symbol.upper(),
        interval=interval,
        limit=limit,
        initial_balance=initial_balance,
    )

    if result is None:
        raise HTTPException(
            status_code=404,
            detail=f"Unable to run backtest for {symbol}",
        )

    return result