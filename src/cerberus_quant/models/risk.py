import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class RiskModel:
    def __init__(self, historical_returns: np.ndarray):
        self.historical_returns = historical_returns

    def historical_var(self, confidence_level: float = 0.99) -> float:
        historical_VaR = np.abs(np.percentile(self.historical_returns, (1 - confidence_level) * 100))
        return historical_VaR

