import numpy as np

import math
import statistics

class ReturnCalculator:
    def __init__(self, prices: list[float]):
        if len(prices) < 2:
            raise ValueError("Need at least two prices to calculate returns.")
        self.prices =  prices

    def simple_returns(self) -> list[float]:
        l1 = []
        for k in range(len(self.prices)-1):
            l1.append(self.prices[k+1]/self.prices[k] - 1)
        
        return l1

    def log_returns(self) -> list[float]:
        l2 = []
        for k in range(len(self.prices)-1):
            l2.append(math.log(self.prices[k+1]/self.prices[k])) 
        
        return l2


if (__name__ == "__main__"):
    calc = ReturnCalculator(prices=[100.0, 150.0, 75.0])
    print(calc.simple_returns())
    print(calc.log_returns())

    print(statistics.mean(calc.simple_returns()))
    print(sum(calc.log_returns()))
