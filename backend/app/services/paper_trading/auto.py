from app.models.auto_trade import AutoTradeResult
from app.models.strategy import Signal
from app.services.paper_trading.orders import order_service
from app.services.strategies import evaluate_strategy


class AutoTradeService:
    """
    Executes a paper trade based on the strategy signal.
    """

    DEFAULT_TRADE_AMOUNT = 1000.0

    def execute(
        self,
        symbol: str,
        amount: float = DEFAULT_TRADE_AMOUNT,
    ) -> AutoTradeResult:

        strategy = evaluate_strategy(symbol)

        order = None

        if strategy.signal == Signal.BUY:

            order = order_service.buy(
                symbol=symbol,
                amount=amount,
            )

        elif strategy.signal == Signal.SELL:

            try:
                order = order_service.sell(symbol)

            except ValueError:
                # Ignore if there is no position to sell
                order = None

        return AutoTradeResult(
            strategy=strategy,
            order=order,
        )


auto_trade_service = AutoTradeService()