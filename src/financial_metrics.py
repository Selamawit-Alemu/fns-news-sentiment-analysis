# financial_metrics.py

import pandas as pd

def calculate_financial_metrics(df: pd.DataFrame) -> dict:
    """
    Calculate key financial metrics from a stock DataFrame.
    Assumes the DataFrame has 'Close' prices.

    Returns a dictionary with volatility, cumulative return, and daily returns Series.
    """
    df = df.copy()
    # Calculate daily returns
    df['daily_returns'] = df['Close'].pct_change()

    # Volatility = std deviation of daily returns
    volatility = df['daily_returns'].std()

    # Cumulative return = product of (1 + daily return) - 1
    cumulative_return = (1 + df['daily_returns']).prod() - 1

    return {
        'volatility': volatility,
        'cumulative_return': cumulative_return,
        'daily_returns': df['daily_returns']
    }
def calculate_financial_metrics(df):
    metrics = {}
    df['daily_returns'] = df['Close'].pct_change()
    metrics['daily_returns'] = df['daily_returns']
    metrics['volatility'] = df['daily_returns'].std()
    metrics['cumulative_return'] = (1 + df['daily_returns']).prod() - 1
    metrics['mean_return'] = df['daily_returns'].mean()
    return metrics
