import matplotlib.pyplot as plt

def plot_sma(df, title="SMA 20"):
    plt.figure(figsize=(12,6))
    plt.plot(df.index, df['Close'], label='Close Price')
    plt.plot(df.index, df['SMA_20'], label='SMA 20')
    plt.title(title)
    plt.legend()
    plt.show()

def plot_rsi(df, title="RSI 14"):
    plt.figure(figsize=(12,4))
    plt.plot(df.index, df['RSI_14'], label='RSI 14', color='orange')
    plt.axhline(70, color='red', linestyle='--')
    plt.axhline(30, color='green', linestyle='--')
    plt.title(title)
    plt.legend()
    plt.show()

def plot_macd(df, title="MACD"):
    plt.figure(figsize=(12,6))
    plt.plot(df.index, df['MACD'], label='MACD')
    plt.plot(df.index, df['MACD_signal'], label='MACD Signal')
    plt.bar(df.index, df['MACD_hist'], label='MACD Hist', alpha=0.3)
    plt.title(title)
    plt.legend()
    plt.show()
