from dotenv import load_dotenv
import os

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "AI Trading OS")
APP_VERSION = os.getenv("APP_VERSION", "0.1.0")
BINANCE_BASE_URL = os.getenv(
    "BINANCE_BASE_URL",
    "https://api.binance.com/api/v3"
)