import pandas as pd
import numpy as np

def momentum_signal(prices, lookback_period=20):
    """
    Generate momentum signals.
    Signal = 1 if current price > price lookback_period days ago, else -1.
    Alternatively, can use returns: Return > 0 -> 1, else -1.
    Here we use a simple price comparison for trend following.
    """
    momentum = prices.pct_change(lookback_period)
    signals = momentum.apply(lambda x: np.where(x > 0, 1, -1))
    return signals

def mean_reversion_signal(prices, window=20, threshold=1.5):
    """
    Generate mean reversion signals using Z-score.
    Z-score = (Price - Moving Average) / Std Dev
    Signal = -1 if Z-score > threshold (Overbought -> Sell)
    Signal = 1 if Z-score < -threshold (Oversold -> Buy)
    Signal = 0 otherwise (Hold/Neutral)
    """
    rolling_mean = prices.rolling(window=window).mean()
    rolling_std = prices.rolling(window=window).std()
    z_score = (prices - rolling_mean) / rolling_std
    
    signals = pd.DataFrame(0, index=prices.index, columns=prices.columns)
    
    # Vectorized signal generation
    signals[z_score > threshold] = -1
    signals[z_score < -threshold] = 1
    
    return signals

def ma_crossover_signal(prices, short_window=20, long_window=60):
    """
    Generate Moving Average Crossover signals.
    Signal = 1 if Short MA > Long MA (Golden Cross -> Buy)
    Signal = -1 if Short MA < Long MA (Death Cross -> Sell)
    """
    short_ma = prices.rolling(window=short_window).mean()
    long_ma = prices.rolling(window=long_window).mean()
    
    signals = pd.DataFrame(0, index=prices.index, columns=prices.columns)
    signals[short_ma > long_ma] = 1
    signals[short_ma < long_ma] = -1
    
    return signals
