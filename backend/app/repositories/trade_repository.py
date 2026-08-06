from sqlalchemy.orm import Session

from app.database import TradeDB


class TradeRepository:
    """
    Repository responsible for
    trade history persistence.
    """

    def save_trade(
        self,
        db: Session,
        trade: TradeDB,
    ) -> TradeDB:
        """
        Save a trade.
        """

        db.add(trade)
        db.commit()
        db.refresh(trade)

        return trade

    def get_trade(
        self,
        db: Session,
        trade_id: int,
    ) -> TradeDB | None:
        """
        Return a trade by ID.
        """

        return (
            db.query(TradeDB)
            .filter(
                TradeDB.id == trade_id
            )
            .first()
        )

    def get_trades(
        self,
        db: Session,
    ) -> list[TradeDB]:
        """
        Return every trade.
        """

        return (
            db.query(TradeDB)
            .all()
        )

    def get_recent(
        self,
        db: Session,
        limit: int = 10,
    ) -> list[TradeDB]:
        """
        Return the most recent trades.
        """

        return (
            db.query(TradeDB)
            .order_by(
                TradeDB.timestamp.desc()
            )
            .limit(limit)
            .all()
        )

    def delete_all(
        self,
        db: Session,
    ) -> None:
        """
        Delete every trade.
        """

        db.query(
            TradeDB
        ).delete()

        db.commit()


trade_repository = TradeRepository()