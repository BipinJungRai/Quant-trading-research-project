import sys
import os
import pandas as pd

# Add the current directory to path so we can import src
sys.path.append(os.getcwd())

from src import data_loader, factors, backtester, metrics

def main():
    # 1. Data Loading
    tickers = ['BTC-USD', 'ETH-USD']
    start_date = '2020-01-01'
    end_date = '2023-12-31'
    
    print(f"Fetching data for {tickers}...")
    prices = data_loader.download_data(tickers, start_date, end_date)
    
    if prices.empty:
        print("No data downloaded. Exiting.")
        return

    print(f"Data shape: {prices.shape}")

    # 2. Strategy Execution
    strategies = {
        'Momentum': factors.momentum_signal(prices),
        'Mean Reversion': factors.mean_reversion_signal(prices),
        'MA Crossover': factors.ma_crossover_signal(prices)
    }

    results = {}
    
    for name, signals in strategies.items():
        print(f"Running backtest for {name}...")
        backtest_res = backtester.run_backtest(prices, signals)
        results[name] = backtest_res['returns']

    # 3. Metrics Calculation
    # Combine all returns into a single DataFrame for metrics calculation
    # Note: backtest returns are DataFrames with columns for each asset. 
    # We might want to aggregate or look at them individually.
    # For simplicity, let's look at the average return across assets for the strategy, 
    # or just list them all.
    
    # Let's create a combined DataFrame where columns are "Strategy_Asset"
    combined_returns = pd.DataFrame()
    
    for strat_name, ret_df in results.items():
        for asset in ret_df.columns:
            combined_returns[f"{strat_name}_{asset}"] = ret_df[asset]
            
    # Add Buy & Hold for comparison
    buy_hold_returns = prices.pct_change().dropna()
    for asset in buy_hold_returns.columns:
        combined_returns[f"Buy&Hold_{asset}"] = buy_hold_returns[asset]

    print("\nCalculating Performance Metrics...")
    perf_metrics = metrics.calculate_metrics(combined_returns)
    
    print("\nPerformance Metrics:")
    print(perf_metrics)

if __name__ == "__main__":
    main()
