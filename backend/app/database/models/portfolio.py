from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import String

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.database.database import Base


class PortfolioAccountDB(Base):
    """
    Paper trading account.
    """

    __tablename__ = "portfolio_accounts"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    cash: Mapped[float] = mapped_column(
        Float,
        default=10000,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    positions: Mapped[list["PortfolioPositionDB"]] = relationship(
        back_populates="account",
        cascade="all, delete-orphan",
    )


class PortfolioPositionDB(Base):
    """
    Current portfolio position.
    """

    __tablename__ = "portfolio_positions"

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

    quantity: Mapped[float] = mapped_column(
        Float
    )

    average_price: Mapped[float] = mapped_column(
        Float
    )

    account: Mapped["PortfolioAccountDB"] = relationship(
        back_populates="positions"
    )