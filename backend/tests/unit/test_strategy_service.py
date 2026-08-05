from app.models.strategy import Signal
from app.services.strategies import evaluate_strategy


class MockRSI:
    def __init__(self, value):
        self.value = value


class MockMACD:
    def __init__(self, histogram):
        self.histogram = histogram


def test_strategy_hold(mocker):
    mocker.patch(
        "app.services.strategies.momentum.get_rsi",
        return_value=[MockRSI(50)],
    )

    mocker.patch(
        "app.services.strategies.momentum.get_macd",
        return_value=[MockMACD(0)],
    )

    result = evaluate_strategy("BTCUSDT")

    assert result.signal == Signal.HOLD
    assert result.confidence == 50


def test_strategy_buy(mocker):
    mocker.patch(
        "app.services.strategies.momentum.get_rsi",
        return_value=[MockRSI(25)],
    )

    mocker.patch(
        "app.services.strategies.momentum.get_macd",
        return_value=[MockMACD(10)],
    )

    result = evaluate_strategy("BTCUSDT")

    assert result.signal == Signal.BUY
    assert result.confidence == 80


def test_strategy_sell(mocker):
    mocker.patch(
        "app.services.strategies.momentum.get_rsi",
        return_value=[MockRSI(75)],
    )

    mocker.patch(
        "app.services.strategies.momentum.get_macd",
        return_value=[MockMACD(-5)],
    )

    result = evaluate_strategy("BTCUSDT")

    assert result.signal == Signal.SELL
    assert result.confidence == 80