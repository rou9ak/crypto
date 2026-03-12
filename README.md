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

## 📊 Sample Results

### 2020 (Bull Market)

Both strategies were highly profitable due to Bitcoin's parabolic run. The MA Crossover slightly outperformed Buy & Hold by sitting out the mid-year dip.

### 2018–2019 (Bear Market)

The MA Crossover strategy substantially outperformed Buy & Hold. By exiting during downtrends, the algorithm preserved capital while pure holders saw steep losses.

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
