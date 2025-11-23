import numpy as np
import pandas as pd

def calculate_metrics(returns, risk_free_rate=0.0):
    """
    Calculate performance metrics.
    
    Args:
        returns (pd.Series or pd.DataFrame): Daily returns.
        risk_free_rate (float): Annual risk-free rate.
        
    Returns:
        pd.DataFrame: Metrics for each column in returns.
    """
    if isinstance(returns, pd.Series):
        returns = returns.to_frame()
        
    metrics = {}
    
    for col in returns.columns:
        r = returns[col].dropna()
        if len(r) == 0:
            continue
            
        # Cumulative Return (CAGR calculation helper)
        total_return = (1 + r).prod() - 1
        n_years = len(r) / 252
        cagr = (1 + total_return) ** (1 / n_years) - 1 if n_years > 0 else 0
        
        # Volatility (Annualized)
        volatility = r.std() * np.sqrt(252)
        
        # Sharpe Ratio
        # Assuming risk_free_rate is annual, convert to daily for calculation or use annualized values
        # Sharpe = (Mean Annual Return - Risk Free) / Annual Std Dev
        mean_annual_return = r.mean() * 252
        sharpe = (mean_annual_return - risk_free_rate) / volatility if volatility != 0 else 0
        
        # Max Drawdown
        cum_returns = (1 + r).cumprod()
        peak = cum_returns.cummax()
        drawdown = (cum_returns - peak) / peak
        max_drawdown = drawdown.min()

        # Sortino Ratio (Downside Deviation)
        downside_returns = r[r < 0]
        downside_vol = downside_returns.std() * np.sqrt(252)
        sortino = (mean_annual_return - risk_free_rate) / downside_vol if downside_vol != 0 else 0

        # Calmar Ratio (CAGR / Max Drawdown)
        calmar = cagr / abs(max_drawdown) if max_drawdown != 0 else 0

        # Win Rate (Daily) - % of days with positive returns
        # Note: This is daily win rate, not per-trade win rate, but useful for vectorised backtest proxy
        win_rate = len(r[r > 0]) / len(r)

        metrics[col] = {
            'CAGR': cagr,
            'Volatility': volatility,
            'Sharpe Ratio': sharpe,
            'Sortino Ratio': sortino,
            'Calmar Ratio': calmar,
            'Max Drawdown': max_drawdown,
            'Win Rate': win_rate
        }
        
    return pd.DataFrame(metrics).T
