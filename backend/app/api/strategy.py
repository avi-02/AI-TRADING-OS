from fastapi import APIRouter

from app.models.strategy import StrategyResult
from app.services.strategies import evaluate_strategy

router = APIRouter(
    prefix="/strategy",
    tags=["Trading Strategy"],
)


@router.get(
    "/{symbol}",
    response_model=StrategyResult,
)
def strategy(symbol: str) -> StrategyResult:
    """
    Evaluate the trading strategy for a symbol.
    """

    return evaluate_strategy(symbol.upper())