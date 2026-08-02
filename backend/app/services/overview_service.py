from app.models.overview import MarketOverview
from app.services.market_service import get_multiple_prices


def get_market_overview() -> MarketOverview:
    """
    Generate a high-level overview of the current market.
    """

    market_data = get_multiple_prices()

    if not market_data:
        raise ValueError("No market data available.")

    highest_price = max(
        market_data,
        key=lambda coin: coin.last_price
    )

    # Highest traded value (USDT), not highest number of coins
    highest_volume = max(
        market_data,
        key=lambda coin: coin.quote_volume
    )

    top_gainer = max(
        market_data,
        key=lambda coin: coin.change_percent
    )

    losers = [
        coin
        for coin in market_data
        if coin.change_percent < 0
    ]

    top_loser = (
        min(
            losers,
            key=lambda coin: coin.change_percent
        )
        if losers
        else None
    )

    return MarketOverview(
        watchlist_size=len(market_data),
        highest_price=highest_price,
        highest_volume=highest_volume,
        top_gainer=top_gainer,
        top_loser=top_loser,
    )