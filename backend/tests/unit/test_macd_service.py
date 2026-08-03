from datetime import UTC, datetime

from app.models.candle import Candle
from app.services.indicators.macd import get_macd


def test_get_macd(mocker):
    candles = [
        Candle(
            open_time=datetime.now(UTC),
            close_time=datetime.now(UTC),
            open_price=float(i),
            high_price=float(i),
            low_price=float(i),
            close_price=float(i),
            volume=100,
            quote_volume=100,
            trade_count=10,
            taker_buy_base_volume=50,
            taker_buy_quote_volume=50,
        )
        for i in range(1, 101)
    ]

    mocker.patch(
        "app.services.indicators.utils.get_candles",
        return_value=candles,
    )

    result = get_macd(
        "BTCUSDT",
        limit=100,
    )

    assert result is not None
    assert len(result) > 0

    first = result[0]

    assert isinstance(first.macd, float)
    assert isinstance(first.signal, float)
    assert isinstance(first.histogram, float)