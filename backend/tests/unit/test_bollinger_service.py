from datetime import UTC, datetime

from app.models.candle import Candle
from app.services.indicators.bollinger import get_bollinger_bands


def test_get_bollinger_bands(mocker):
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

    result = get_bollinger_bands(
        "BTCUSDT",
        period=20,
        limit=100,
    )

    assert result is not None
    assert len(result) > 0

    first = result[0]

    assert first.upper_band > first.middle_band
    assert first.middle_band > first.lower_band