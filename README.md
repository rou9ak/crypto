# 📈 Cryptocurrency Trading Algorithm in Python

A guided project implementing a **Moving Average Crossover** algorithmic trading strategy on Bitcoin-USD market data using `yfinance`, `pandas`, `numpy`, and `matplotlib`.

---

## 🗂️ Project Structure

```
crypto-trading-algo/
├── crypto_trading_algorithm.ipynb   # Main Jupyter notebook
├── requirements.txt                 # Python dependencies
├── .gitignore                       # Files to ignore in version control
└── README.md                        # Project documentation
```

---

## 🧠 What This Project Covers

| Section | Description |
|---|---|
| **Data Fetching** | Pull historical BTC-USD price data via `yfinance` |
| **EDA & Visualization** | Plot price charts and Simple Moving Averages (SMA) |
| **Strategy Design** | Implement the Moving Average Crossover strategy |
| **Signal Generation** | Compute buy/sell trade signals using SMA crossovers |
| **Backtesting** | Simulate portfolio performance on historical data |
| **Performance Comparison** | Compare algorithm returns vs. Buy-and-Hold baseline |

---

## 🔧 Strategy: Moving Average Crossover

The algorithm uses **two Simple Moving Averages (SMAs)** with different time windows:

- **Short-term SMA** (10-day window) — reacts quickly to price changes
- **Long-term SMA** (40-day window) — reflects broader trend

**Rules:**
- 🟢 **BUY** — when the short-term SMA crosses *above* the long-term SMA (bullish signal)
- 🔴 **SELL** — when the short-term SMA crosses *below* the long-term SMA (bearish signal)

---

## 📊 Backtest Results (2020 BTC-USD)

Both strategies were simulated starting with **$10,000 USD** over the full calendar year 2020.

| Strategy | Outcome |
|---|---|
| Buy and Hold | ~4× return (driven by Bitcoin's year-end rally) |
| Moving Avg Crossover | Slightly outperforms Buy-and-Hold; avoids some downside |

> ⚠️ **Disclaimer:** Past performance does not guarantee future results. This project is for educational purposes only and is not financial advice.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- Jupyter Notebook or JupyterLab

### Installation

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/crypto-trading-algo.git
cd crypto-trading-algo

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the notebook
jupyter notebook crypto_trading_algorithm.ipynb
```

---

## 📦 Dependencies

| Library | Purpose |
|---|---|
| `yfinance` | Fetch historical market data from Yahoo Finance |
| `pandas` | Data manipulation and analysis |
| `numpy` | Numerical computations |
| `matplotlib` | Plotting price charts and strategy visualizations |

---

## 💡 Extending the Project

Some ideas to take this further:

- **Tune the SMA windows** — Try different `short_interval` / `long_interval` combinations and see how performance changes
- **Test other time periods** — The notebook exercise suggests backtesting over 2018–2019, a bear market year
- **Try other cryptocurrencies** — Replace `"BTC-USD"` with `"ETH-USD"`, `"SOL-USD"`, etc.
- **Add transaction costs** — Simulate realistic broker fees to get more accurate backtest results
- **Implement forward testing** — Paper-trade the algorithm with real-time data using a simulated balance

---

## ⚠️ A Note on Backtesting

Backtesting tells you how a strategy *would have* performed — it does not predict future returns. Be especially careful about **overfitting**: tuning parameters to maximize historical performance often leads to strategies that fail on unseen data. Always forward-test before committing real capital.

---

## 📚 Resources

- [yfinance Documentation](https://pypi.org/project/yfinance/)
- [Moving Average Crossover — Wikipedia](https://en.wikipedia.org/wiki/Moving_average_crossover)
- [Backtesting — Investopedia](https://www.investopedia.com/terms/b/backtesting.asp)
- [Moving Averages in Forex — Investopedia](https://www.investopedia.com/ask/answers/122314/how-do-i-use-moving-average-ma-create-forex-trading-strategy.asp)

---

## 👤 Original Author

[David Pasternak](https://www.linkedin.com/in/david-pasternak-6b84a2208/) — IBM Skills Network Guided Project

## 📝 License

This project is for educational purposes. Original course content © 2021 IBM Corporation.
