from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import String

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from app.database.database import Base


class TradeDB(Base):
    """
    Trade history.
    """

    __tablename__ = "trades"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    account_id: Mapped[int] = mapped_column(
        ForeignKey("portfolio_accounts.id")
    )

    symbol: Mapped[str] = mapped_column(
        String(20)
    )

    side: Mapped[str] = mapped_column(
        String(10)
    )

    price: Mapped[float] = mapped_column(
        Float
    )

    quantity: Mapped[float] = mapped_column(
        Float
    )

    status: Mapped[str] = mapped_column(
        String(20)
    )

    timestamp: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )