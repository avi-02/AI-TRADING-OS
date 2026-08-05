from app.models.strategy import Signal


def simulate_trades(
    prices: list[float],
    signals: list[Signal],
    initial_balance: float = 10_000,
) -> tuple[
    float,
    int,
    int,
    int,
]:
    """
    Simulate simple BUY/SELL trading.

    Rules:
    - Buy with all available cash.
    - Sell entire position.
    - Ignore fees and slippage.
    """

    cash = initial_balance
    position = 0.0

    total_trades = 0
    winning_trades = 0
    losing_trades = 0

    entry_price = 0.0

    for price, signal in zip(prices, signals):

        if signal == Signal.BUY and cash > 0:

            position = cash / price
            cash = 0.0
            entry_price = price

            total_trades += 1

        elif signal == Signal.SELL and position > 0:

            cash = position * price

            if price > entry_price:
                winning_trades += 1
            else:
                losing_trades += 1

            position = 0.0

    if position > 0:
        cash = position * prices[-1]

    return (
        cash,
        total_trades,
        winning_trades,
        losing_trades,
    )