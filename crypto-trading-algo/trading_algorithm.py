"""
Cryptocurrency Moving Average Crossover Trading Algorithm
=========================================================
IBM Skills Network Guided Project — Completed Portfolio Version

Author:    Rounak
Course:    Create a Cryptocurrency Trading Algorithm in Python
           (IBM / Cognitive Class)

Description:
    Fetches BTC-USD historical data via yfinance, computes Simple
    Moving Averages, generates buy/sell signals using the Moving
    Average Crossover strategy, and backtests performance against
    a Buy-and-Hold baseline.

Usage:
    python trading_algorithm.py
    python trading_algorithm.py --start 2018-01-01 --end 2019-12-31
"""

import argparse
import os

import numpy as np
import pandas as pd
import yfinance as yf
from matplotlib import pyplot as plt
from matplotlib.dates import DateFormatter


# ──────────────────────────────────────────────
# Configuration defaults
# ──────────────────────────────────────────────
TICKER          = "BTC-USD"
DEFAULT_START   = "2020-01-01"
DEFAULT_END     = "2020-12-31"
SHORT_WINDOW    = 10       # days
LONG_WINDOW     = 40       # days
INITIAL_CAPITAL = 10_000.0 # USD
CHARTS_DIR      = "charts"


# ──────────────────────────────────────────────
# Data fetching
# ──────────────────────────────────────────────
def fetch_data(ticker: str, start: str, end: str) -> pd.DataFrame:
    """Download daily OHLCV data from Yahoo Finance."""
    print(f"[INFO] Downloading {ticker} from {start} to {end} ...")
    df = yf.download(ticker, start=start, end=end, interval="1d")
    print(f"[INFO] Retrieved {len(df)} trading days.")
    return df


# ──────────────────────────────────────────────
# Signal generation
# ──────────────────────────────────────────────
def generate_signals(
    price_data: pd.DataFrame,
    short_window: int = SHORT_WINDOW,
    long_window: int = LONG_WINDOW,
) -> pd.DataFrame:
    """
    Compute SMAs and generate Moving Average Crossover trade signals.

    Returns a DataFrame with columns:
        Short     — short-term SMA
        Long      — long-term SMA
        Signal    — 1.0 when short > long, else 0.0
        Position  — +1.0 (buy), -1.0 (sell), 0.0 (hold)
    """
    signals = pd.DataFrame(index=price_data.index)
    signals["Short"]    = price_data["Close"].rolling(window=short_window, min_periods=1).mean()
    signals["Long"]     = price_data["Close"].rolling(window=long_window,  min_periods=1).mean()
    signals["Signal"]   = np.where(signals["Short"] > signals["Long"], 1.0, 0.0)
    signals["Position"] = signals["Signal"].diff()
    return signals


# ──────────────────────────────────────────────
# Backtesting
# ──────────────────────────────────────────────
def backtest(
    price_data: pd.DataFrame,
    signals: pd.DataFrame,
    capital: float = INITIAL_CAPITAL,
) -> pd.DataFrame:
    """
    Simulate the strategy on historical data.

    Assumptions:
        - Portfolio is fully in BTC or fully in USD at all times.
        - Zero-commission trades.
        - Trades execute at the closing price of the signal day.
    """
    bt = pd.DataFrame(index=signals.index)
    bt["BTC_Return"] = price_data["Close"] / price_data["Close"].shift(1)
    bt["Alg_Return"] = np.where(signals["Signal"] == 1, bt["BTC_Return"], 1.0)
    bt["Algo"]       = capital * bt["Alg_Return"].cumprod()
    bt["BuyHold"]    = capital * bt["BTC_Return"].cumprod()
    return bt


# ──────────────────────────────────────────────
# Plotting helpers
# ──────────────────────────────────────────────
def _fmt_axis(ax, fig):
    date_format = DateFormatter("%b-%d-%y")
    ax.xaxis.set_major_formatter(date_format)
    ax.tick_params(axis="x", labelsize=7)
    fig.autofmt_xdate()


def plot_price_chart(price_data: pd.DataFrame, title: str = "BTC-USD Closing Price") -> None:
    fig, ax = plt.subplots(dpi=130)
    _fmt_axis(ax, fig)
    ax.plot(price_data["Close"], lw=0.75, color="steelblue", label="Closing Price")
    ax.set_ylabel("Price (USD)")
    ax.set_title(title)
    ax.grid(alpha=0.4)
    ax.legend()
    plt.tight_layout()
    _save(fig, "01_price_chart.png")
    plt.show()


def plot_sma(price_data: pd.DataFrame, signals: pd.DataFrame, short_window: int, long_window: int) -> None:
    fig, ax = plt.subplots(dpi=130)
    _fmt_axis(ax, fig)
    ax.plot(price_data["Close"],  lw=0.75, label="Closing Price")
    ax.plot(signals["Short"],     lw=0.75, alpha=0.8, label=f"{short_window}-Day SMA")
    ax.plot(signals["Long"],      lw=0.75, alpha=0.8, label=f"{long_window}-Day SMA")
    ax.set_ylabel("Price (USD)")
    ax.set_title("BTC-USD with Simple Moving Averages")
    ax.grid(alpha=0.4)
    ax.legend()
    plt.tight_layout()
    _save(fig, "02_sma_chart.png")
    plt.show()


def plot_signals(price_data: pd.DataFrame, signals: pd.DataFrame, short_window: int, long_window: int) -> None:
    fig, ax = plt.subplots(dpi=130)
    _fmt_axis(ax, fig)
    ax.plot(price_data["Close"], lw=0.75, label="Closing Price")
    ax.plot(signals["Short"], lw=0.75, alpha=0.75, color="orange", label=f"{short_window}-Day SMA (Short)")
    ax.plot(signals["Long"],  lw=0.75, alpha=0.75, color="purple", label=f"{long_window}-Day SMA (Long)")
    ax.plot(
        signals[signals["Position"] ==  1.0].index,
        signals["Short"][signals["Position"] ==  1.0],
        marker=6, ms=5, ls="none", color="green", label="Buy",
    )
    ax.plot(
        signals[signals["Position"] == -1.0].index,
        signals["Short"][signals["Position"] == -1.0],
        marker=7, ms=5, ls="none", color="red", label="Sell",
    )
    ax.set_ylabel("Price (USD)")
    ax.set_title("Moving Average Crossover — Buy/Sell Signals")
    ax.grid(alpha=0.4)
    ax.legend(fontsize=7)
    plt.tight_layout()
    _save(fig, "03_signals_chart.png")
    plt.show()


def plot_backtest(bt: pd.DataFrame, capital: float) -> None:
    fig, ax = plt.subplots(dpi=130)
    _fmt_axis(ax, fig)
    ax.plot(bt["BuyHold"], lw=0.75, label="Buy & Hold")
    ax.plot(bt["Algo"],    lw=0.75, label="MA Crossover Strategy")
    ax.axhline(y=capital, color="grey", linestyle="--", lw=0.6, label="Initial Capital")
    ax.set_ylabel("Portfolio Value (USD)")
    ax.set_title("Backtest: MA Crossover vs Buy & Hold")
    ax.grid(alpha=0.4)
    ax.legend()
    plt.tight_layout()
    _save(fig, "04_backtest_chart.png")
    plt.show()


def _save(fig, filename: str) -> None:
    os.makedirs(CHARTS_DIR, exist_ok=True)
    path = os.path.join(CHARTS_DIR, filename)
    fig.savefig(path, dpi=130, bbox_inches="tight")
    print(f"[INFO] Chart saved → {path}")


# ──────────────────────────────────────────────
# Performance summary
# ──────────────────────────────────────────────
def print_summary(bt: pd.DataFrame, signals: pd.DataFrame, capital: float, start: str, end: str) -> None:
    final_algo    = bt["Algo"].iloc[-1]
    final_buyhold = bt["BuyHold"].iloc[-1]
    algo_return   = (final_algo    - capital) / capital * 100
    bh_return     = (final_buyhold - capital) / capital * 100
    n_buys        = len(signals[signals["Position"] ==  1.0])
    n_sells       = len(signals[signals["Position"] == -1.0])

    print("\n" + "=" * 50)
    print("        BACKTEST RESULTS")
    print("=" * 50)
    print(f"  Period             : {start}  →  {end}")
    print(f"  Starting Capital   : ${capital:>10,.2f}")
    print(f"  MA Crossover Final : ${final_algo:>10,.2f}  ({algo_return:+.2f}%)")
    print(f"  Buy & Hold Final   : ${final_buyhold:>10,.2f}  ({bh_return:+.2f}%)")
    print(f"  Buy Orders         : {n_buys}")
    print(f"  Sell Orders        : {n_sells}")
    print("=" * 50 + "\n")


# ──────────────────────────────────────────────
# CLI entry-point
# ──────────────────────────────────────────────
def parse_args():
    parser = argparse.ArgumentParser(description="BTC Moving Average Crossover Backtest")
    parser.add_argument("--start",   default=DEFAULT_START,   help="Start date YYYY-MM-DD")
    parser.add_argument("--end",     default=DEFAULT_END,     help="End date YYYY-MM-DD")
    parser.add_argument("--short",   default=SHORT_WINDOW,    type=int, help="Short SMA window (days)")
    parser.add_argument("--long",    default=LONG_WINDOW,     type=int, help="Long SMA window (days)")
    parser.add_argument("--capital", default=INITIAL_CAPITAL, type=float, help="Starting capital in USD")
    parser.add_argument("--no-plot", action="store_true",     help="Skip chart rendering")
    return parser.parse_args()


def main():
    args = parse_args()

    price_data = fetch_data(TICKER, args.start, args.end)
    signals    = generate_signals(price_data, args.short, args.long)
    bt         = backtest(price_data, signals, args.capital)

    if not args.no_plot:
        plot_price_chart(price_data)
        plot_sma(price_data, signals, args.short, args.long)
        plot_signals(price_data, signals, args.short, args.long)
        plot_backtest(bt, args.capital)

    print_summary(bt, signals, args.capital, args.start, args.end)


if __name__ == "__main__":
    main()
