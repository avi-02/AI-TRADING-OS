from datetime import UTC, datetime

from fastapi.testclient import TestClient

from app.main import app
from app.models.candle import Candle

client = TestClient(app)


def test_get_candles_api(mocker):
    sample = [
        Candle(
            open_time=datetime.fromtimestamp(
                1719936000000 / 1000,
                tz=UTC,
            ),
            close_time=datetime.fromtimestamp(
                1719939599999 / 1000,
                tz=UTC,
            ),
            open_price=63100.0,
            high_price=63350.0,
            low_price=62990.0,
            close_price=63280.0,
            volume=1523.44,
            quote_volume=96200000.0,
            trade_count=58234,
            taker_buy_base_volume=712.32,
            taker_buy_quote_volume=44900000.0,
        )
    ]

    mocker.patch(
        "app.api.market.get_candles",
        return_value=sample,
    )

    response = client.get(
        "/candles/BTCUSDT?interval=1h&limit=1"
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1
    assert data[0]["open_price"] == 63100.0
    assert data[0]["close_price"] == 63280.0
    assert data[0]["trade_count"] == 58234