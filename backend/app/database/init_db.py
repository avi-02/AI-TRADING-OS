from app.database import (
    Base,
    engine,
)

# Import models so SQLAlchemy registers them
from app.database import (
    PortfolioAccountDB,
    PortfolioPositionDB,
    TradeDB,
)


def init_database() -> None:
    """
    Create all database tables.
    """

    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_database()

    print("Database initialized successfully.")