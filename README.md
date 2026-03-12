# 📈 Cryptocurrency Moving Average Crossover Trading Algorithm

> **IBM Skills Network Guided Project** — *Create a Cryptocurrency Trading Algorithm in Python*

A Python implementation of the **Moving Average Crossover** algorithmic trading strategy applied to Bitcoin (BTC-USD) historical data. Includes data fetching, market analysis, signal generation, backtesting, and multi-period comparison — fully runnable as a Jupyter Notebook or standalone Python script.

---

## 🗂️ Project Structure

```
crypto-trading-algo/
├── crypto_trading_algorithm.ipynb   # Main notebook (completed, with all solutions)
├── trading_algorithm.py             # Standalone CLI script
├── requirements.txt                 # Python dependencies
├── charts/                          # Auto-generated chart outputs
│   ├── 01_price_chart.png
│   ├── 02_sma_chart.png
│   ├── 03_signals_chart.png
│   └── 04_backtest_chart.png
└── README.md
```

---

## 📚 What This Project Covers

| Topic | Description |
|---|---|
| **Data Fetching** | Pull BTC-USD OHLCV data via `yfinance` |
| **Exploratory Analysis** | Line charts, OHLCV column inspection |
| **Simple Moving Averages** | Rolling mean over configurable windows |
| **Crossover Strategy** | Buy/sell signal generation from SMA crossovers |
| **Backtesting** | Simulate strategy on historical data with P&L tracking |
| **Comparison** | MA Crossover vs Buy-and-Hold baseline across bull & bear markets |

---

## 🧠 Strategy — Moving Average Crossover

Two SMAs are computed over the BTC closing price:

- **Short SMA** (default: 10 days) — reacts quickly to price changes
- **Long SMA** (default: 40 days) — reveals longer-term trends

**Signals:**
- 🟢 **Buy** — Short SMA crosses *above* Long SMA (bullish momentum)
- 🔴 **Sell** — Short SMA crosses *below* Long SMA (bearish reversal)
- ⬜ **Hold cash** — between signals; portfolio value stays flat

---

## 🚀 Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/<your-username>/crypto-trading-algo.git
cd crypto-trading-algo
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3a. Run the Jupyter Notebook

```bash
jupyter notebook crypto_trading_algorithm.ipynb
```

### 3b. Run the CLI script

```bash
# Default: 2020 BTC-USD, $10,000 starting capital
python trading_algorithm.py

# Custom date range and SMA windows
python trading_algorithm.py --start 2018-01-01 --end 2019-12-31 --short 10 --long 40

# Skip chart rendering (useful for CI)
python trading_algorithm.py --no-plot
```

---

## 📊 Charts & Results

### 1. BTC-USD Closing Price — 2020

![BTC-USD Closing Price](charts/01_price_chart.png)

Bitcoin started 2020 around $7,000, dipped sharply during the COVID crash in March, consolidated through mid-year, then surged dramatically in Q4 — nearly reaching $30,000 by year-end.

---

### 2. BTC-USD with Simple Moving Averages

![BTC-USD with SMAs](charts/02_sma_chart.png)

The **10-day SMA** (orange) closely tracks the closing price, while the **40-day SMA** (green) smooths out short-term noise and reveals the broader trend. The growing divergence between the two SMAs in Q4 signals strong bullish momentum.

---

### 3. Moving Average Crossover — Buy/Sell Signals

![Buy/Sell Signals](charts/03_signals_chart.png)

🟢 **Green triangles** mark buy orders (short SMA crosses above long SMA).  
🔴 **Red triangles** mark sell orders (short SMA crosses below long SMA).  
The algorithm correctly avoided the March crash by issuing a sell signal, and re-entered before the Q4 bull run.

---

### 4. Backtest: MA Crossover vs Buy & Hold

![Backtest Results](charts/04_backtest_chart.png)

Both strategies delivered strong returns in 2020 due to Bitcoin's parabolic Q4 run. The **MA Crossover strategy** (orange) slightly outperformed **Buy & Hold** (blue) by sitting out the mid-year correction — ultimately growing a $10,000 starting portfolio to over **$42,000**.

> These results are **historical** and **do not guarantee future returns.**

---

## 📦 Dependencies

| Library | Version | Purpose |
|---|---|---|
| `yfinance` | ≥ 0.2.18 | Market data from Yahoo Finance |
| `pandas` | ≥ 1.3.0 | DataFrame manipulation |
| `numpy` | ≥ 1.21.0 | Vectorised signal computation |
| `matplotlib` | ≥ 3.4.0 | Chart rendering |

---

## ⚠️ Disclaimer

This project is for **educational purposes only**. The strategies implemented here are simplified and are **not** financial advice. Backtested performance does not guarantee future results. Never invest money you can't afford to lose.

---

## 🔗 References

- [yfinance — PyPI](https://pypi.org/project/yfinance/)
- [Moving Average Crossover — Investopedia](https://www.investopedia.com/ask/answers/122314/how-do-i-use-moving-average-ma-create-forex-trading-strategy.asp)
- [Backtesting — Investopedia](https://www.investopedia.com/terms/b/backtesting.asp)
- [Moving Average Crossover — Wikipedia](https://en.wikipedia.org/wiki/Moving_average_crossover)
- IBM Skills Network Guided Project, original author: David Pasternak (2021)

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).
