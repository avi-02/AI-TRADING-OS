from datetime import datetime

from pydantic import BaseModel


class SMAValue(BaseModel):
    """
    Represents one Simple Moving Average value.
    """

    timestamp: datetime
    value: float


class EMAValue(BaseModel):
    """
    Represents one Exponential Moving Average value.
    """

    timestamp: datetime
    value: float


class RSIValue(BaseModel):
    """
    Represents one RSI value.
    """

    timestamp: datetime
    value: float

class MACDValue(BaseModel):
    """
    Represents one MACD data point.
    """

    timestamp: datetime

    macd: float
    signal: float
    histogram: float 

class BollingerBandValue(BaseModel):
    """
    Represents one Bollinger Band data point.
    """

    timestamp: datetime

    upper_band: float
    middle_band: float
    lower_band: float