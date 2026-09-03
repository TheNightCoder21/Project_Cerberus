import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf


from src.cerberus_quant.data.market_data import MarketDataFetcher
from src.cerberus_quant.data.synthetic import SyntheticDataGen
from src.cerberus_quant.data.returns import ReturnCalculator
from src.cerberus_quant.models.risk import RiskModel
from src.cerberus_quant.models.volatility import VolatilityModel


class Backtest:
    def __init__(self, ticker: str, start_date: str, end_date: str):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.window_size = 1000
        self.confidence_level = 0.99

    def run_backtest(self):
        fetcher = MarketDataFetcher(data_source="yfinance")
        data = fetcher.fetch_data(ticker=self.ticker, start_date=self.start_date, end_date=self.end_date)
        log_returns_real = ReturnCalculator(prices=data).log_returns()
        volatilityModel = VolatilityModel(log_returns_real)
        ewma_var = volatilityModel.ewma_variance(lambda_=0.94)

        # mu_actual = np.mean(log_returns_real)
        # sigma_actual = np.std(log_returns_real)

        
        hit_count1 = 0
        hit_count2 = 0
        tot_pred = 0

        for i in range(self.window_size, len(log_returns_real)):
            hist = log_returns_real[i - self.window_size : i]
            risk= RiskModel(historical_returns=hist)
            hist_var = risk.historical_var(confidence_level=self.confidence_level)
            actual_return = log_returns_real[i]
            curr_volatility = np.sqrt(ewma_var[i-1])
            Ewma_var = risk.parametric_var(current_volatility=curr_volatility, confidence_level=self.confidence_level)
            if (actual_return < -hist_var):
                hit_count1 += 1
            if (actual_return < -Ewma_var):
                hit_count2 += 1
            tot_pred += 1

        hit_rate1 = hit_count1 / (len(data) - self.window_size)
        hit_rate2 = hit_count2 / (len(data) - self.window_size)
        return hit_rate1, hit_rate2;

if __name__ == "__main__":
    backtest = Backtest(ticker="SPY", start_date="2000-01-01", end_date="2024-01-01")
    hit_rate1, hit_rate2 = backtest.run_backtest()
    print(f"actual Hit Rate of the Historical VaR model on the S&P 500: {hit_rate1:.2%}")
    print(f"actual Hit Rate of the EWMA VaR model on the S&P 500: {hit_rate2:.2%}")
    print(f"Expected Hit Rate at 99% confidence: {1 - 0.99:.2%}")