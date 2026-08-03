from datetime import UTC, datetime

from app.models.candle import Candle
from app.services import market_service


def sample_candles():
    return [
        [
            1719936000000,
            "63100.00",
            "63350.00",
            "62990.00",
            "63280.00",
            "1523.44",
            1719939599999,
            "96200000",
            58234,
            "712.32",
            "44900000",
            "0",
        ]
    ]


def test_get_candles(mocker):
    mocker.patch(
        "app.services.market_service.fetch_candles",
        return_value=sample_candles(),
    )

    candles = market_service.get_candles(
        "BTCUSDT",
        interval="1h",
        limit=1,
    )

    assert candles is not None
    assert len(candles) == 1

    candle = candles[0]

    assert isinstance(candle, Candle)
    assert candle.open_price == 63100.0
    assert candle.high_price == 63350.0
    assert candle.low_price == 62990.0
    assert candle.close_price == 63280.0
    assert candle.trade_count == 58234
    assert candle.open_time == datetime.fromtimestamp(
        1719936000000 / 1000,
        tz=UTC,
    )