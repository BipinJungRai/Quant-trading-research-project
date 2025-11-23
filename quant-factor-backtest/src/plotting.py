import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def plot_equity_curves(equity_curves, title="Equity Curves"):
    """
    Plot equity curves for multiple strategies/assets.
    """
    plt.figure(figsize=(12, 6))
    for col in equity_curves.columns:
        plt.plot(equity_curves.index, equity_curves[col], label=col)
    
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Equity ($)")
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_drawdowns(returns, title="Drawdowns"):
    """
    Plot drawdown curves.
    """
    plt.figure(figsize=(12, 6))
    
    for col in returns.columns:
        cum_returns = (1 + returns[col]).cumprod()
        peak = cum_returns.cummax()
        drawdown = (cum_returns - peak) / peak
        plt.plot(drawdown.index, drawdown, label=col)
        
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Drawdown (%)")
    plt.legend()
    plt.grid(True)
    plt.show()
