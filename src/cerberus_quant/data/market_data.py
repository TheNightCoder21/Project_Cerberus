import numpy as np
import yfinance as yf
import pandas as pd
from yfinance import ticker

class MarketDataFetcher:
    def __init__(self, data_source):
        self.data_source = data_source

    def fetch_data(self, ticker: str, start_date: str, end_date: str) -> np.ndarray:

        df = yf.download(ticker, start=start_date, end=end_date)
                
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        if 'Adj Close' in df.columns:
            target_col = 'Adj Close'
        elif 'Close' in df.columns:
            target_col = 'Close'
        else:
            raise KeyError(f"Data schema changed! Available columns are: {df.columns}")
            
        return df[target_col].dropna().values



if __name__ == "__main__":
    fetcher = MarketDataFetcher(data_source="yfinance")
    data = fetcher.fetch_data(ticker="SPY", start_date="2000-01-01", end_date="2024-01-01")
    log_returns = np.log(data[1:] / data[:-1])
    print("Log Returns of Real Data:", log_returns)