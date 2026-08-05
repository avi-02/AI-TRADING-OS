from app.models.pnl import PortfolioSummary
from app.services.market_service import get_price
from app.services.paper_trading.portfolio import (
    portfolio_service,
)


INITIAL_CASH = 10000.0


class PnLService:
    """
    Calculates live portfolio performance.
    """

    def get_summary(self) -> PortfolioSummary:
        """
        Return the current portfolio summary.
        """

        portfolio = portfolio_service.get_portfolio()

        market_value = 0.0

        for position in portfolio.positions:

            ticker = get_price(position.symbol)

            if ticker is None:
                continue

            market_value += (
                position.quantity
                * ticker.last_price
            )

        portfolio_value = (
            portfolio.cash
            + market_value
        )

        profit = (
            portfolio_value
            - INITIAL_CASH
        )

        profit_percent = (
            (profit / INITIAL_CASH) * 100
        )

        return PortfolioSummary(
            cash=round(portfolio.cash, 2),
            market_value=round(market_value, 2),
            portfolio_value=round(portfolio_value, 2),
            profit=round(profit, 2),
            profit_percent=round(
                profit_percent,
                2,
            ),
            total_positions=len(
                portfolio.positions
            ),
        )


pnl_service = PnLService()