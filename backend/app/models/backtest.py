from pydantic import BaseModel


class BacktestResult(BaseModel):
    """
    Backtesting summary.
    """

    symbol: str

    strategy: str

    initial_balance: float

    final_balance: float

    profit_percent: float

    total_trades: int

    winning_trades: int

    losing_trades: int

    win_rate: float