import requests

from app.config.settings import BINANCE_BASE_URL
from app.core.logger import logger


class MarketRepository:
    """
    Repository responsible for communicating
    with the Binance Market API.
    """

    def fetch_price(
        self,
        symbol: str,
    ):
        logger.info(
            f"Calling Binance API for {symbol}"
        )

        url = (
            f"{BINANCE_BASE_URL}/ticker/24hr"
            f"?symbol={symbol}"
        )

        response = requests.get(url)

        if response.status_code != 200:
            logger.error(
                f"Binance returned {response.status_code} for {symbol}"
            )
            return None

        return response.json()

    def fetch_candles(
        self,
        symbol: str,
        interval: str = "1h",
        limit: int = 100,
    ):
        """
        Fetch historical candlestick data.
        """

        url = (
            f"{BINANCE_BASE_URL}/klines"
            f"?symbol={symbol}"
            f"&interval={interval}"
            f"&limit={limit}"
        )

        logger.info(
            f"Fetching {limit} candles for {symbol} ({interval})"
        )

        response = requests.get(url)

        if response.status_code != 200:
            logger.error(
                f"Failed to fetch candles for {symbol}"
            )
            return None

        return response.json()


market_repository = MarketRepository()