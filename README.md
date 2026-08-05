# 🚀 AI Trading OS

> A production-ready algorithmic trading backend built with **FastAPI**, featuring technical indicators, strategy evaluation, historical backtesting, and a modular architecture ready for AI-powered trading.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-009688)
![Pytest](https://img.shields.io/badge/Tests-30%20Passed-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📌 Overview

AI Trading OS is a modular backend platform for algorithmic trading.

The system fetches live market data, calculates technical indicators, evaluates trading strategies, performs historical backtesting, and exposes everything through REST APIs.

The architecture has been designed with scalability in mind so future AI models, portfolio management, and paper trading can be integrated without major refactoring.

---

# ✨ Features

## 📈 Market Data

- Live Market Prices
- Historical Candlestick Data
- Multiple Timeframes

---

## 📊 Technical Indicators

- ✅ Simple Moving Average (SMA)
- ✅ Exponential Moving Average (EMA)
- ✅ Relative Strength Index (RSI)
- ✅ Moving Average Convergence Divergence (MACD)
- ✅ Bollinger Bands

---

## 🤖 Trading Strategy

Current Strategy:

- Momentum Strategy
    - RSI
    - MACD
    - Buy/Sell/Hold Signals

---

## 📉 Backtesting Engine

- Historical Simulation
- Trade Execution
- Profit Calculation
- Win Rate
- Trade Statistics

Example:

```json
{
    "symbol": "BTCUSDT",
    "strategy": "Momentum",
    "profit_percent": 0.11,
    "win_rate": 50
}
```

---

# 🏗 Architecture

```
                    Binance API
                         │
                         ▼
                  Repository Layer
                         │
                         ▼
                  Service Layer
      ┌──────────┬───────────┬───────────┐
      ▼          ▼           ▼
 Indicators   Scanner    Strategies
      │
      ▼
 Backtesting Engine
      │
      ▼
     FastAPI
      │
      ▼
 REST API + Swagger
```

---

# 📂 Project Structure

```
backend/
│
├── app/
│   ├── api/
│   ├── models/
│   ├── repositories/
│   ├── services/
│   │   ├── indicators/
│   │   ├── strategies/
│   │   └── backtesting/
│   ├── config.py
│   └── main.py
│
├── tests/
│   ├── integration/
│   └── unit/
│
├── requirements.txt
├── pytest.ini
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/AI-Trading-OS.git

cd AI-Trading-OS/backend
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate

### macOS/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Server

```bash
uvicorn app.main:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

Swagger UI

---

# 🧪 Running Tests

```bash
pytest
```

Current Status

```
30 Passed
```

---

# 📡 API Endpoints

## Market

```
GET /market/price/{symbol}
GET /market/candles/{symbol}
```

---

## Overview

```
GET /overview/{symbol}
```

---

## Scanner

```
GET /scanner/top-gainers
GET /scanner/top-losers
```

---

## Indicators

```
GET /indicator/sma/{symbol}
GET /indicator/ema/{symbol}
GET /indicator/rsi/{symbol}
GET /indicator/macd/{symbol}
GET /indicator/bollinger/{symbol}
```

---

## Strategy

```
GET /strategy/{symbol}
```

---

## Backtesting

```
GET /backtest/{symbol}
```

---

# 🧪 Test Coverage

The project includes:

- Unit Tests
- Integration Tests
- API Tests

Current Status

```
30 Passing Tests
```

---

# 🛠 Tech Stack

Backend

- Python 3.11
- FastAPI
- Pydantic
- Uvicorn

Testing

- Pytest
- FastAPI TestClient

Data

- Binance Market API

Architecture

- Layered Architecture
- Repository Pattern
- Service Layer

---

# 🚀 Roadmap

## Version 1.0 ✅

- Live Market Data
- Indicators
- Strategy Engine
- Backtesting
- REST APIs

---

## Version 2 🚧

- Paper Trading
- Portfolio Management
- Order Book
- Trade History

---

## Version 3 🤖

- AI Price Prediction
- LSTM Models
- Transformer Models
- Sentiment Analysis

---

## Version 4 📊

- Dashboard
- Authentication
- WebSockets
- Live Charts

---

# 📸 Screenshots

## Swagger UI

_Add screenshot here_

---

## Backtest API

_Add screenshot here_

---

## Strategy API

_Add screenshot here_

---

# 👨‍💻 Author

**Avikshit Diwakar Kharkar**

Machine Learning Engineer | Data Science | Algorithmic Trading

GitHub:
https://github.com/<your-github>

LinkedIn:
https://linkedin.com/in/<your-linkedin>

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---

# 📄 License

This project is licensed under the MIT License.