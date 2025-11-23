# Quant Trading Research Project

## Overview
This repository hosts quantitative trading research, including backtesting engines, strategy implementations, and research documentation.

## Project Structure

### 1. Codebase: `quant-factor-backtest/`
This directory contains the core Python implementation for factor-based backtesting.
- **Strategies**: Momentum, Mean Reversion, Moving Average Crossover.
- **Assets**: BTC-USD, ETH-USD.
- **Components**:
    - `src/`: Data loading, factor computation, backtesting logic.
    - `notebooks/`: Interactive research and analysis (e.g., `factor_research.ipynb`).

### 2. Research Documentation
- **Research Paper**: A detailed PDF covering the thought process, methodology, and findings will be available in this root directory.

## Strategies Implemented
- **Momentum**: Trend following based on lookback periods.
- **Mean Reversion**: Contrarian strategy using Z-scores of price deviations.
- **Moving Average Crossover**: Classic trend following using short and long term moving averages.

## Dataset
- **Source**: Yahoo Finance (`yfinance`)
- **Assets**: BTC-USD, ETH-USD
- **Period**: 2017 to Present (configurable)

## How to Run

1. Navigate to the code directory:
   ```bash
   cd quant-factor-backtest
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the research notebook:
   - Launch Jupyter Lab or Notebook.
   - Open `notebooks/factor_research.ipynb`.
   - Run all cells to execute the backtest and view results.

## Example Results
The notebook provides detailed equity curves, drawdown charts, and a performance metrics table (Sharpe Ratio, CAGR, Volatility, Max Drawdown) comparing all strategies against a Buy & Hold benchmark.
