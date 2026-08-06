from datetime import datetime

from app.database import SessionLocal
from app.database.models.trade import TradeDB
from app.models.portfolio import (
    OrderResponse,
    Position,
)
from app.repositories.trade_repository import (
    trade_repository,
)
from app.services.market_service import get_price
from app.services.paper_trading.portfolio import (
    portfolio_service,
)


class OrderService:
    """
    Executes paper trading BUY and SELL orders.
    """

    def buy(
        self,
        symbol: str,
        amount: float,
    ) -> OrderResponse:
        """
        Execute a BUY order.
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

            position = Position(
                symbol=symbol,
                quantity=quantity,
                average_price=current_price,
            )

        else:

            total_quantity = (
                position.quantity + quantity
            )

            total_cost = (
                position.quantity
                * position.average_price
            ) + amount

            position.average_price = (
                total_cost / total_quantity
            )

            position.quantity = total_quantity

        portfolio_service.save_position(position)

        remaining_cash = (
            portfolio.cash - amount
        )

        portfolio_service.update_cash(
            remaining_cash
        )

        db = SessionLocal()

        try:

            account_id = (
                portfolio_service.get_account_id()
            )

            trade_repository.save_trade(
                db,
                TradeDB(
                    account_id=account_id,
                    symbol=symbol,
                    side="BUY",
                    price=current_price,
                    quantity=quantity,
                    status="FILLED",
                    timestamp=datetime.utcnow(),
                ),
            )

        finally:
            db.close()

        return OrderResponse(
            symbol=symbol,
            side="BUY",
            price=current_price,
            quantity=quantity,
            remaining_cash=remaining_cash,
            status="FILLED",
        )

    def sell(
        self,
        symbol: str,
        quantity: float | None = None,
    ) -> OrderResponse:
        """
        Execute a SELL order.
        """

        portfolio = portfolio_service.get_portfolio()

        position = portfolio_service.get_position(
            symbol
        )

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

        proceeds = (
            quantity * current_price
        )

        remaining_cash = (
            portfolio.cash + proceeds
        )

        position.quantity -= quantity

        if position.quantity <= 0:

            portfolio_service.remove_position(
                symbol
            )

        else:

            portfolio_service.save_position(
                position
            )

        portfolio_service.update_cash(
            remaining_cash
        )

        db = SessionLocal()

        try:

            account_id = (
                portfolio_service.get_account_id()
            )

            trade_repository.save_trade(
                db,
                TradeDB(
                    account_id=account_id,
                    symbol=symbol,
                    side="SELL",
                    price=current_price,
                    quantity=quantity,
                    status="FILLED",
                    timestamp=datetime.utcnow(),
                ),
            )

        finally:
            db.close()

        return OrderResponse(
            symbol=symbol,
            side="SELL",
            price=current_price,
            quantity=quantity,
            remaining_cash=remaining_cash,
            status="FILLED",
        )


order_service = OrderService()