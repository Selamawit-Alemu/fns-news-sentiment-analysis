import talib
import pandas as pd

def calculate_sma(df, period=20):
    return talib.SMA(df['Close'], timeperiod=period)

def calculate_rsi(df, period=14):
    return talib.RSI(df['Close'], timeperiod=period)

def calculate_macd(df):
    macd, signal, hist = talib.MACD(df['Close'])
    return macd, signal, hist

def add_indicators(df):
    """
    Add SMA, RSI, and MACD indicators to the DataFrame.
    Args:
        df (pd.DataFrame): Stock price data with 'Close' column.
    Returns:
        pd.DataFrame: DataFrame with added indicator columns.
    """
    df = df.copy()
    df['SMA_20'] = calculate_sma(df, 20)
    df['RSI_14'] = calculate_rsi(df, 14)
    df['MACD'], df['MACD_signal'], df['MACD_hist'] = calculate_macd(df)
    return df
