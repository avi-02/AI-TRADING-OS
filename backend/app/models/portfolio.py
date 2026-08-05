from pydantic import BaseModel, Field


class Position(BaseModel):
    """
    Represents an open paper trading position.
    """

    symbol: str
    quantity: float = Field(
        gt=0,
        description="Quantity currently held.",
    )
    average_price: float = Field(
        gt=0,
        description="Average purchase price.",
    )


class Portfolio(BaseModel):
    """
    Represents the current paper trading portfolio.
    """

    cash: float = Field(
        ge=0,
        description="Available cash balance.",
    )

    positions: list[Position] = Field(
        default_factory=list,
        description="Current open positions.",
    )


class OrderRequest(BaseModel):
    """
    Request body for placing a paper trade.
    """

    amount: float = Field(
        gt=0,
        description="Amount of cash to invest.",
    )


class OrderResponse(BaseModel):
    """
    Response returned after executing a paper order.
    """

    symbol: str
    side: str
    price: float = Field(
        gt=0,
        description="Executed market price.",
    )
    quantity: float = Field(
        gt=0,
        description="Executed quantity.",
    )
    remaining_cash: float = Field(
        ge=0,
        description="Cash remaining after the order.",
    )
    status: str