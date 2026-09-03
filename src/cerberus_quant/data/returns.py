import numpy as np

import math
import statistics

class ReturnCalculator:
    def __init__(self, prices: np.ndarray):
        if len(prices) < 2:
            raise ValueError("Need at least two prices to calculate returns.")
        self.prices =  np.asarray(prices)

    def simple_returns(self) -> np.ndarray:
        return (self.prices[1:] - self.prices[:-1]) / self.prices[:-1]

    def log_returns(self) -> np.ndarray:
        return np.log(self.prices[1:] / self.prices[:-1])


if (__name__ == "__main__"):
    calc = ReturnCalculator(prices=[100.0, 150.0, 75.0])
    print(calc.simple_returns())
    print(calc.log_returns())

    print(statistics.mean(calc.simple_returns()))
    print(sum(calc.log_returns()))
