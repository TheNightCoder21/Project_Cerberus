import numpy as np

import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt

class SyntheticDataGen:
    def __init__(self):
        pass

    def gen_gaussian_prices(self, initial_price: float, mu: float, sigma: float, days: int) -> np.ndarray:
        self.initial_price = initial_price
        self.mu = mu
        self.sigma = sigma
        self.days = days

        log_returns = np.random.normal(loc=mu, scale=sigma, size=days)

        cumulative_returns = np.cumsum(log_returns)

        price_path = initial_price * np.exp(cumulative_returns)

        return price_path 


if __name__ == "__main__":
    synth = SyntheticDataGen()
    prices = synth.gen_gaussian_prices(initial_price=100.0, mu=0.0001, sigma=0.01, days=10000)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(prices, color='blue', linewidth=0.5)
    ax1.set_title("Simulated Price Path (Random Walk)")
    ax1.set_xlabel("Days")
    ax1.set_ylabel("Price")

    log_returns = np.log(prices[1:] / prices[:-1])
    ax2.hist(log_returns, bins=50, density=True, alpha=0.5, color='g')
    ax2.set_title("Distribution of Log Returns (Bell Curve)")
    ax2.set_xlabel("Log Returns")
    ax2.set_ylabel("Density")

    plt.tight_layout()
    plt.show()