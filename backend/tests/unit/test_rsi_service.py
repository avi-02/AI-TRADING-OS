from datetime import UTC, datetime

from app.models.candle import Candle
from app.services.indicators.rsi import get_rsi


def test_get_rsi(mocker):
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
        for i in range(1, 40)
    ]

    mocker.patch(
        "app.services.indicators.utils.get_candles",
        return_value=candles,
    )

    result = get_rsi(
        "BTCUSDT",
        period=14,
        limit=39,
    )

    assert result is not None
    assert len(result) > 0

    for value in result:
        assert 0 <= value.value <= 100