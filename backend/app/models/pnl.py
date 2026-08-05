from pydantic import BaseModel, Field


class PortfolioSummary(BaseModel):
    """
    Summary of the current paper trading portfolio.
    """

    cash: float = Field(
        ge=0,
        description="Available cash balance.",
    )

    market_value: float = Field(
        ge=0,
        description="Current market value of all positions.",
    )

    portfolio_value: float = Field(
        ge=0,
        description="Cash + market value.",
    )

    profit: float = Field(
        description="Overall profit or loss.",
    )

    profit_percent: float = Field(
        description="Overall return percentage.",
    )

    total_positions: int = Field(
        ge=0,
        description="Number of open positions.",
    )