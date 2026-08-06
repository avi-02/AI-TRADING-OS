from sqlalchemy.orm import Session

from app.database import (
    PortfolioAccountDB,
    PortfolioPositionDB,
)


class PortfolioRepository:
    """
    Repository responsible for managing
    paper trading portfolio persistence.
    """

    # ==========================================================
    # Account
    # ==========================================================

    def get_account(
        self,
        db: Session,
    ) -> PortfolioAccountDB | None:
        """
        Return the paper trading account.
        """

        return db.query(
            PortfolioAccountDB
        ).first()

    def account_exists(
        self,
        db: Session,
    ) -> bool:
        """
        Return True if an account exists.
        """

        return self.get_account(db) is not None

    def create_account(
        self,
        db: Session,
        initial_cash: float = 10000,
    ) -> PortfolioAccountDB:
        """
        Create a new paper trading account.
        """

        account = PortfolioAccountDB(
            cash=initial_cash,
        )

        db.add(account)
        db.commit()
        db.refresh(account)

        return account

    def get_or_create_account(
        self,
        db: Session,
        initial_cash: float = 10000,
    ) -> PortfolioAccountDB:
        """
        Return an existing account or create one.
        """

        account = self.get_account(db)

        if account is None:
            account = self.create_account(
                db,
                initial_cash,
            )

        return account

    def update_cash(
        self,
        db: Session,
        account: PortfolioAccountDB,
        cash: float,
    ) -> PortfolioAccountDB:
        """
        Update account cash.
        """

        account.cash = cash

        db.commit()
        db.refresh(account)

        return account

    def reset_account(
        self,
        db: Session,
        initial_cash: float = 10000,
    ) -> PortfolioAccountDB:
        """
        Reset account cash and remove all positions.
        """

        account = self.get_or_create_account(
            db,
            initial_cash,
        )

        self.clear_positions(
            db,
            account.id,
        )

        return self.update_cash(
            db,
            account,
            initial_cash,
        )

    # ==========================================================
    # Positions
    # ==========================================================

    def get_position(
        self,
        db: Session,
        account_id: int,
        symbol: str,
    ) -> PortfolioPositionDB | None:
        """
        Return a position by symbol.
        """

        return (
            db.query(PortfolioPositionDB)
            .filter(
                PortfolioPositionDB.account_id == account_id,
                PortfolioPositionDB.symbol == symbol,
            )
            .first()
        )

    def get_positions(
        self,
        db: Session,
        account_id: int,
    ) -> list[PortfolioPositionDB]:
        """
        Return every position for an account.
        """

        return (
            db.query(PortfolioPositionDB)
            .filter(
                PortfolioPositionDB.account_id == account_id
            )
            .all()
        )

    def save_position(
        self,
        db: Session,
        position: PortfolioPositionDB,
    ) -> PortfolioPositionDB:
        """
        Save or update a position.
        """

        db.add(position)
        db.commit()
        db.refresh(position)

        return position

    def delete_position(
        self,
        db: Session,
        position: PortfolioPositionDB,
    ) -> None:
        """
        Delete a position.
        """

        db.delete(position)
        db.commit()

    def clear_positions(
        self,
        db: Session,
        account_id: int,
    ) -> None:
        """
        Delete all positions for an account.
        """

        (
            db.query(PortfolioPositionDB)
            .filter(
                PortfolioPositionDB.account_id == account_id
            )
            .delete()
        )

        db.commit()


portfolio_repository = PortfolioRepository()