import yfinance as yf
import pandas as pd
import os

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
    # Define data directory relative to this script
    # src/data_loader.py -> parent is src -> parent is project root -> data is in project root/data
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, 'data')
    file_path = os.path.join(data_dir, 'prices.csv')

    # Ensure data directory exists
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Check if cache exists
    if os.path.exists(file_path):
        print(f"Loading data from cache: {file_path}")
        data = pd.read_csv(file_path, index_col=0, parse_dates=True)
        return data

    print(f"Downloading data for {tickers} from {start_date} to {end_date}...")
    data = yf.download(tickers, start=start_date, end=end_date)['Close']
    
    # If only one ticker, yfinance might return a Series or DataFrame without MultiIndex columns
    # We want to ensure a DataFrame structure
    if isinstance(data, pd.Series):
        data = data.to_frame()
        data.columns = tickers
        
    data = data.dropna()
    
    # Save to cache
    data.to_csv(file_path)
    print(f"Data saved to cache: {file_path}")
    
    print("Data download complete.")
    return data
