# 🚀 AI Trading OS

> An AI-powered algorithmic trading platform built with **FastAPI**, **Python**, and **Binance Market Data**.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green)
![Tests](https://img.shields.io/badge/Tests-44_Passing-success)
![License](https://img.shields.io/badge/License-MIT-orange)

---

# 📌 Overview

AI Trading OS is a modular trading platform designed to analyze cryptocurrency markets, generate trading signals, perform historical backtesting, and simulate paper trading.

The project is built with clean architecture principles, comprehensive automated testing, and CI/CD using GitHub Actions.

---

# ✨ Features

## 📈 Market Data

- Live Binance Market Data
- Historical Candle Data
- Market Overview API
- Crypto Scanner

---

## 📊 Technical Indicators

- Simple Moving Average (SMA)
- Exponential Moving Average (EMA)
- Relative Strength Index (RSI)
- MACD
- Bollinger Bands

---

## 🤖 Strategy Engine

- Momentum Strategy
- BUY / SELL / HOLD Signals
- Confidence Score
- Strategy Reasoning

---

## 📉 Backtesting Engine

- Historical Simulation
- Portfolio Growth
- Win Rate
- Profit %
- Trade Statistics

---

## 💰 Paper Trading

- Portfolio Management
- Paper BUY Orders
- Paper SELL Orders
- Live Portfolio P&L
- Automatic Strategy Execution

---

## 🌐 REST APIs

- Market APIs
- Indicator APIs
- Scanner APIs
- Strategy APIs
- Backtesting APIs
- Paper Trading APIs

---

## 🧪 Testing

- 44 Automated Tests
- Unit Tests
- Integration Tests
- GitHub Actions CI

---

# 🏗 Architecture

```
                        AI Trading OS

                           FastAPI
                              │
      ┌───────────────────────┼────────────────────────┐
      │                       │                        │
      ▼                       ▼                        ▼
 Market APIs          Strategy APIs          Paper Trading APIs
      │                       │                        │
      ▼                       ▼                        ▼
 Market Service      Momentum Strategy        Portfolio Service
      │                       │                        │
      ▼                       ▼                        ▼
 Binance API          Indicators          Order & PnL Engine
```

---

# 📂 Project Structure

```
AI-Trading-OS
│
├── backend
│   ├── app
│   │   ├── api
│   │   ├── models
│   │   ├── services
│   │   ├── repositories
│   │   └── utils
│   │
│   └── tests
│
├── .github
├── README.md
├── CHANGELOG.md
└── LICENSE
```

---

# 🚀 Getting Started

## Clone

```bash
git clone https://github.com/YOUR_USERNAME/AI-Trading-OS.git
```

## Install

```bash
cd backend

python -m venv venv

source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the server

```bash
uvicorn app.main:app --reload
```

Open Swagger

```
http://127.0.0.1:8000/docs
```

---

# 📊 Current Statistics

| Metric | Value |
|---------|------:|
| APIs | 20+ |
| Technical Indicators | 5 |
| Strategies | 1 |
| Backtesting Engine | ✅ |
| Paper Trading | ✅ |
| Tests | 44 |
| CI/CD | GitHub Actions |

---

# 🛣 Roadmap

## ✅ Sprint 1–10

- Project Setup
- Market Data APIs
- Technical Indicators
- Scanner
- Strategy Engine
- Backtesting Engine
- Paper Trading
- Auto Trading
- 44 Automated Tests

---

## 🚧 Sprint 11

- SQLite Database
- SQLAlchemy ORM
- Portfolio Persistence
- Trade History

---

## 🔮 Future

- Multiple Trading Strategies
- Machine Learning Predictions
- Authentication
- PostgreSQL
- Docker
- Kubernetes
- React Dashboard
- WebSockets
- Real-Time Charts

---

# 🤝 Contributing

Contributions are welcome.

Please open an issue before submitting major changes.

---

# 📜 License

MIT License

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.