from pydantic import BaseModel

from app.models.portfolio import OrderResponse
from app.models.strategy import StrategyResult


class AutoTradeResult(BaseModel):
    """
    Result of an automatic paper trade.
    """

    strategy: StrategyResult
    order: OrderResponse | None