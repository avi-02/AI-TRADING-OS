from app.models.portfolio import (
    Portfolio,
    Position,
)


class PortfolioService:
    """
    Manages the paper trading portfolio.
    """

    def __init__(
        self,
        initial_cash: float = 10000,
    ):
        self._portfolio = Portfolio(
            cash=initial_cash,
            positions=[],
        )

    def get_portfolio(self) -> Portfolio:
        """
        Return the current portfolio.
        """

        return self._portfolio

    def reset(
        self,
        initial_cash: float = 10000,
    ) -> Portfolio:
        """
        Reset the portfolio.
        """

        self._portfolio = Portfolio(
            cash=initial_cash,
            positions=[],
        )

        return self._portfolio

    def get_position(
        self,
        symbol: str,
    ) -> Position | None:
        """
        Return an existing position.
        """

        for position in self._portfolio.positions:
            if position.symbol == symbol:
                return position

        return None


portfolio_service = PortfolioService()