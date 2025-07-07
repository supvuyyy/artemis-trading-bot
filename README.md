# Artemis: Python-Based Commodity Trading Bot

**Artemis** is a momentum-based algorithmic trading bot built in Python that analyzes crude oil price movements using technical indicators. It identifies buy/sell signals based on RSI and moving average crossovers, visualizes trades, and backtests performance on historical data.

---

## Strategy Overview

- **Buy Signal:**
  - RSI < 30 (oversold)
  - 10-day Moving Average crosses **above** 30-day Moving Average

- **Sell Signal:**
  - RSI > 70 (overbought)
  - 10-day MA crosses **below** 30-day MA

This dual-confirmation system attempts to catch early momentum reversals.

---

##  Tools & Libraries

- `Python 3`
- `pandas` — data manipulation
- `yfinance` — historical market data
- `matplotlib` — visualizing trade signals
- `numpy` — numerical calculations

---

##  Backtest Performance

- Time period: 2020–2024 crude oil futures
- Achieved **~20% ROI** in a simulated environment
- Signals were visualized and overlaid on price charts for review

###  Example Output

![Trade Signals](artemis_signals.png)

---

## 📄 Research Whitepaper

A full technical write-up of the Artemis strategy — including trade logic, backtest results, and expansion ideas — will be available soon.

> _Coming soon: whitepaper.pdf_

---

##  Future Plans

- Deploy strategy with **Alpaca API** for live paper trading
- Add support for **SPY**, **QQQ**, and other ETFs
- Experiment with **machine learning (Random Forest)** for signal optimization
- Include performance metrics: **Sharpe ratio, drawdowns, win/loss rate**

---

##  About the Project

Artemis was independently developed as a personal exploration into quantitative trading and algorithmic strategy design. It is part of a broader initiative to apply data science in real-world finance and demonstrate technical fluency in a self-driven research context.

---

## License

This project is open for educational use and personal experimentation. No financial advice provided.
