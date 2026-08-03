from datetime import UTC, datetime

from app.models.candle import Candle
from app.services.indicators.sma import get_sma


def test_get_sma(mocker):
    candles = [
        Candle(
            open_time=datetime.now(UTC),
            close_time=datetime.now(UTC),
            open_price=i,
            high_price=i,
            low_price=i,
            close_price=float(i),
            volume=100,
            quote_volume=100,
            trade_count=10,
            taker_buy_base_volume=50,
            taker_buy_quote_volume=50,
        )
        for i in range(1, 21)
    ]

    mocker.patch(
        "app.services.indicators.utils.get_candles",
        return_value=candles,
    )

    result = get_sma(
        "BTCUSDT",
        period=5,
        limit=20,
    )

    assert result is not None
    assert len(result) == 16
    assert result[-1].value == 18.0