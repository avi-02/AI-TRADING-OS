from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to AI Trading OS 🚀"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_price():
    response = client.get("/price/BTCUSDT")

    assert response.status_code == 200

    data = response.json()

    assert data["symbol"] == "BTCUSDT"
    assert data["last_price"] > 0
    assert data["high_price"] >= data["low_price"]
    assert data["volume"] >= 0
    assert isinstance(data["trade_count"], int)