import numpy as np
import pandas as pd

import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt

from scipy.stats import skew, kurtosis
import yfinance as yf

from src.cerberus_quant.data.market_data import MarketDataFetcher
from src.cerberus_quant.data.synthetic import SyntheticDataGen
from src.cerberus_quant.data.returns import ReturnCalculator
from src.cerberus_quant.models.risk import RiskModel



if __name__ == "__main__":
    fetcher = MarketDataFetcher(data_source="yfinance")
    data = fetcher.fetch_data(ticker="SPY", start_date="2000-01-01", end_date="2024-01-01")
    log_returns_real = ReturnCalculator(prices=data).log_returns()

    mu_actual = np.mean(log_returns_real)
    sigma_actual = np.std(log_returns_real)

    synth = SyntheticDataGen()
    prices_synth = synth.gen_gaussian_prices(initial_price=100.0, mu=mu_actual, sigma=sigma_actual, days=len(data))
    log_returns_synth = ReturnCalculator(prices=prices_synth).log_returns()

    hist_model_real = RiskModel(historical_returns=log_returns_real)
    print(f"Historical VaR (Real Data) at 99% confidence: {hist_model_real.historical_var(confidence_level=0.99)}")

    # print(f"Skewness of Real Data Log Returns: {skew(log_returns_real)} whereas Skewness of Synthetic Data Log Returns: {skew(log_returns_synth)}")
    # print(f"Kurtosis of Real Data Log Returns: {kurtosis(log_returns_real)} whereas Kurtosis of Synthetic Data Log Returns: {kurtosis(log_returns_synth)}")

    # fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # ax1.hist(log_returns_real, bins=100, density=True, alpha=0.5, color='b', label='Real Data')
    # ax2.hist(log_returns_synth, bins=100, density=True, alpha=0.5, color='r', label='Synthetic Data')
    # ax1.set_xlabel('Log Returns')
    # ax1.set_ylabel('Density')
    # ax1.set_title('Distribution of Log Returns (Real Data)')
    # ax2.set_xlabel('Log Returns')
    # ax2.set_ylabel('Density')
    # ax2.set_title('Distribution of Log Returns (Synthetic Data)')

    # plt.tight_layout()
    # plt.show()