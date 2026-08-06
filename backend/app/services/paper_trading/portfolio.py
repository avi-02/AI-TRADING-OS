from app.database import SessionLocal
from app.database.models.portfolio import PortfolioPositionDB
from app.models.portfolio import (
    Portfolio,
    Position,
)
from app.repositories.portfolio_repository import (
    portfolio_repository,
)


class PortfolioService:
    """
    Manages the paper trading portfolio using SQLite.
    """

    def get_portfolio(self) -> Portfolio:
        db = SessionLocal()

        try:
            account = portfolio_repository.get_or_create_account(db)

            positions_db = portfolio_repository.get_positions(
                db,
                account.id,
            )

            positions = [
                Position(
                    symbol=position.symbol,
                    quantity=position.quantity,
                    average_price=position.average_price,
                )
                for position in positions_db
            ]

            return Portfolio(
                cash=account.cash,
                positions=positions,
            )

        finally:
            db.close()

    def reset(
        self,
        initial_cash: float = 10000,
    ) -> Portfolio:
        db = SessionLocal()

        try:
            account = portfolio_repository.reset_account(
                db,
                initial_cash,
            )

            return Portfolio(
                cash=account.cash,
                positions=[],
            )

        finally:
            db.close()

    def get_position(
        self,
        symbol: str,
    ) -> Position | None:
        db = SessionLocal()

        try:
            account = portfolio_repository.get_or_create_account(db)

            position = portfolio_repository.get_position(
                db,
                account.id,
                symbol,
            )

            if position is None:
                return None

            return Position(
                symbol=position.symbol,
                quantity=position.quantity,
                average_price=position.average_price,
            )

        finally:
            db.close()

    def save_position(
        self,
        position: Position,
    ) -> None:
        db = SessionLocal()

        try:
            account = portfolio_repository.get_or_create_account(db)

            existing = portfolio_repository.get_position(
                db,
                account.id,
                position.symbol,
            )

            if existing is None:

                existing = PortfolioPositionDB(
                    account_id=account.id,
                    symbol=position.symbol,
                    quantity=position.quantity,
                    average_price=position.average_price,
                )

            else:

                existing.quantity = position.quantity
                existing.average_price = (
                    position.average_price
                )

            portfolio_repository.save_position(
                db,
                existing,
            )

        finally:
            db.close()

    def remove_position(
        self,
        symbol: str,
    ) -> None:
        db = SessionLocal()

        try:
            account = portfolio_repository.get_or_create_account(db)

            position = portfolio_repository.get_position(
                db,
                account.id,
                symbol,
            )

            if position:

                portfolio_repository.delete_position(
                    db,
                    position,
                )

        finally:
            db.close()

    def update_cash(
        self,
        cash: float,
    ) -> None:
        db = SessionLocal()

        try:
            account = portfolio_repository.get_or_create_account(db)

            portfolio_repository.update_cash(
                db,
                account,
                cash,
            )

        finally:
            db.close()

    def get_account_id(self) -> int:
        """
        Return the database account id.
        """

        db = SessionLocal()

        try:
            account = portfolio_repository.get_or_create_account(db)

            return account.id

        finally:
            db.close()


portfolio_service = PortfolioService()