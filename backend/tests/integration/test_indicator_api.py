from datetime import UTC, datetime

from fastapi.testclient import TestClient

from app.main import app
from app.models.indicator import (
    EMAValue,
    MACDValue,
    RSIValue,
    SMAValue,
)

client = TestClient(app)


def test_sma_api(mocker):
    mocker.patch(
        "app.api.indicator.get_sma",
        return_value=[
            SMAValue(
                timestamp=datetime.now(UTC),
                value=100.5,
            )
        ],
    )

    response = client.get("/indicator/sma/BTCUSDT")

    assert response.status_code == 200
    assert response.json()[0]["value"] == 100.5


def test_ema_api(mocker):
    mocker.patch(
        "app.api.indicator.get_ema",
        return_value=[
            EMAValue(
                timestamp=datetime.now(UTC),
                value=101.2,
            )
        ],
    )

    response = client.get("/indicator/ema/BTCUSDT")

    assert response.status_code == 200
    assert response.json()[0]["value"] == 101.2


def test_rsi_api(mocker):
    mocker.patch(
        "app.api.indicator.get_rsi",
        return_value=[
            RSIValue(
                timestamp=datetime.now(UTC),
                value=56.3,
            )
        ],
    )

    response = client.get("/indicator/rsi/BTCUSDT")

    assert response.status_code == 200
    assert response.json()[0]["value"] == 56.3

def test_macd_api(mocker):
    mocker.patch(
        "app.api.indicator.get_macd",
        return_value=[
            MACDValue(
                timestamp=datetime.now(UTC),
                macd=12.5,
                signal=10.2,
                histogram=2.3,
            )
        ],
    )

    response = client.get("/indicator/macd/BTCUSDT")

    assert response.status_code == 200

    data = response.json()

    assert data[0]["macd"] == 12.5
    assert data[0]["signal"] == 10.2
    assert data[0]["histogram"] == 2.3