# Quant Factor Backtest Project

## Project Goal
This project implements a factor-based backtesting system for cryptocurrencies (BTC-USD, ETH-USD). It explores three common quantitative trading strategies:
1. **Momentum**: Trend following based on lookback periods.
2. **Mean Reversion**: Contrarian strategy using Z-scores of price deviations.
3. **Moving Average Crossover**: Classic trend following using short and long term moving averages.

## Dataset
- **Source**: Yahoo Finance (`yfinance`)
- **Assets**: BTC-USD, ETH-USD
- **Period**: 2017 to Present (configurable)

## Strategies Implemented
- **Momentum**: Buys when positive trend is detected over `n` days.
- **Mean Reversion**: Buys when price is statistically oversold (Z-score < -threshold) and sells when overbought (Z-score > threshold).
- **MA Crossover**: Buys when Short MA > Long MA, Sells when Short MA < Long MA.

## Project Structure
- `data/`: Directory for storing data (if needed).
- `notebooks/`: Jupyter notebooks for research and analysis.
- `src/`: Python source code for data loading, factor calculation, backtesting, metrics, and plotting.

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Navigate to `notebooks/` and open `factor_research.ipynb`.
3. Run all cells to execute the backtest and view results.

## Example Results
The notebook provides detailed equity curves, drawdown charts, and a performance metrics table (Sharpe Ratio, CAGR, Volatility, Max Drawdown) comparing all strategies against a Buy & Hold benchmark.
