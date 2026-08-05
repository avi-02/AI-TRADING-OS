from enum import Enum

from pydantic import BaseModel


class Signal(str, Enum):
    BUY = "BUY"
    SELL = "SELL"
    HOLD = "HOLD"


class StrategyResult(BaseModel):
    """
    Trading strategy result.
    """

    symbol: str

    signal: Signal

    confidence: int

    reasons: list[str]