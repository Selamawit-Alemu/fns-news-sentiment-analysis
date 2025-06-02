import os
import pandas as pd

def load_all_stock_data(folder_path='data/yfinance_data'):
    """
    Load all CSVs from the specified folder into a dictionary of stock DataFrames.
    
    Returns:
        dict[str, pd.DataFrame]: Dictionary with keys as stock tickers and values as DataFrames.
    """
    stock_data = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            ticker = filename.split('_')[0]  # e.g., 'AAPL_historical_data.csv' -> 'AAPL'
            filepath = os.path.join(folder_path, filename)
            df = pd.read_csv(filepath, parse_dates=True, index_col=0)  # Assuming first column is Date
            stock_data[ticker] = df
    return stock_data
