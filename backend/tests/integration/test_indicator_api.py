from datetime import UTC, datetime

from fastapi.testclient import TestClient

from app.main import app
from app.models.indicator import EMAValue, RSIValue, SMAValue

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