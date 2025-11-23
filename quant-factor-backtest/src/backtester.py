import pandas as pd
import numpy as np

def run_backtest(prices, signals, initial_capital=10000.0, transaction_cost=0.001):
    """
    Run a simple vectorised backtest.
    
    Args:
        prices (pd.DataFrame): Asset prices.
        signals (pd.DataFrame): Trading signals (-1, 0, 1).
        initial_capital (float): Starting capital.
        transaction_cost (float): Cost per trade (e.g., 0.1% = 0.001).
        
    Returns:
        dict: Dictionary containing 'returns', 'equity_curve', 'positions'.
    """
    # Shift signals by 1 to avoid lookahead bias (we trade at Close based on signal from previous Close or Open of current day)
    # Assuming we trade at the Close of the day the signal is generated, but in reality we'd trade next open.
    # For simplicity in daily data backtesting, we often shift signal to apply to next day's return.
    
    # Calculate daily returns of the asset
    asset_returns = prices.pct_change()
    
    # Align signals: Signal calculated at t applies to return at t+1
    # lagged_signals = signals.shift(1) 
    # However, if we assume we trade AT the close when signal is generated, we get the return of the NEXT day.
    
    lagged_signals = signals.shift(1)
    
    # Strategy returns = Signal * Asset Returns
    strategy_returns = lagged_signals * asset_returns
    
    # Transaction costs
    # Trades occur when signal changes
    trades = signals.diff().abs()
    # Cost is proportional to the position change magnitude
    # This is a simplified cost model.
    costs = trades * transaction_cost
    
    # Net strategy returns (approximate)
    net_strategy_returns = strategy_returns - costs.shift(1).fillna(0) # Costs apply when trade happens, affecting subsequent PnL? 
    # Actually, costs reduce capital at the moment of trade.
    # Simplified: subtract cost from return of that day (or next day depending on execution)
    # Let's subtract cost from the day the trade is effective (t+1)
    
    net_strategy_returns = net_strategy_returns.fillna(0)
    
    # Calculate Equity Curve
    cumulative_returns = (1 + net_strategy_returns).cumprod()
    equity_curve = initial_capital * cumulative_returns
    
    return {
        'returns': net_strategy_returns,
        'equity_curve': equity_curve,
        'signals': signals
    }
