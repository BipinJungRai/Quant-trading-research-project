import yfinance as yf
import pandas as pd

def download_data(tickers, start_date, end_date):
    """
    Download historical data for given tickers.
    
    Args:
        tickers (list): List of ticker strings (e.g., ['BTC-USD', 'ETH-USD']).
        start_date (str): Start date in 'YYYY-MM-DD' format.
        end_date (str): End date in 'YYYY-MM-DD' format.
        
    Returns:
        pd.DataFrame: DataFrame containing Close prices for the tickers.
    """
    print(f"Downloading data for {tickers} from {start_date} to {end_date}...")
    data = yf.download(tickers, start=start_date, end=end_date)['Close']
    
    # If only one ticker, yfinance might return a Series or DataFrame without MultiIndex columns
    # We want to ensure a DataFrame structure
    if isinstance(data, pd.Series):
        data = data.to_frame()
        data.columns = tickers
        
    data = data.dropna()
    print("Data download complete.")
    return data
