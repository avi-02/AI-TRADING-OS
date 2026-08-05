from app.models.portfolio import (
    OrderResponse,
    Position,
)
from app.services.market_service import get_price
from app.services.paper_trading.portfolio import (
    portfolio_service,
)


class OrderService:
    """
    Executes paper trading buy and sell orders.
    """

    def buy(
        self,
        symbol: str,
        amount: float,
    ) -> OrderResponse:
        """
        Execute a paper BUY order.
        """

        portfolio = portfolio_service.get_portfolio()

        if amount > portfolio.cash:
            raise ValueError(
                "Insufficient cash balance."
            )

        ticker = get_price(symbol)

        if ticker is None:
            raise ValueError(
                f"Unable to fetch price for {symbol}"
            )

        current_price = ticker.last_price

        quantity = amount / current_price

        position = portfolio_service.get_position(symbol)

        if position is None:
            portfolio.positions.append(
                Position(
                    symbol=symbol,
                    quantity=quantity,
                    average_price=current_price,
                )
            )
        else:
            total_quantity = (
                position.quantity + quantity
            )

            total_cost = (
                position.quantity * position.average_price
            ) + amount

            position.average_price = (
                total_cost / total_quantity
            )

            position.quantity = total_quantity

        portfolio.cash -= amount

        return OrderResponse(
            symbol=symbol,
            side="BUY",
            price=current_price,
            quantity=quantity,
            remaining_cash=portfolio.cash,
            status="FILLED",
        )

    def sell(
        self,
        symbol: str,
        quantity: float | None = None,
    ) -> OrderResponse:
        """
        Execute a paper SELL order.
        """

        portfolio = portfolio_service.get_portfolio()

        position = portfolio_service.get_position(symbol)

        if position is None:
            raise ValueError(
                f"No position found for {symbol}"
            )

        ticker = get_price(symbol)

        if ticker is None:
            raise ValueError(
                f"Unable to fetch price for {symbol}"
            )

        current_price = ticker.last_price

        if quantity is None:
            quantity = position.quantity

        if quantity > position.quantity:
            raise ValueError(
                "Not enough quantity available."
            )

        proceeds = quantity * current_price

        portfolio.cash += proceeds

        position.quantity -= quantity

        if position.quantity <= 0:
            portfolio.positions.remove(position)

        return OrderResponse(
            symbol=symbol,
            side="SELL",
            price=current_price,
            quantity=quantity,
            remaining_cash=portfolio.cash,
            status="FILLED",
        )


order_service = OrderService()