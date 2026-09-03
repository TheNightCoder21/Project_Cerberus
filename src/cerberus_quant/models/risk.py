import numpy as np
import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt


class RiskModel:
    def __init__(self, historical_returns: np.ndarray):
        self.historical_returns = np.asarray(historical_returns)

    def historical_var(self, confidence_level: float = 0.99) -> float:
        historical_VaR = -(np.percentile(self.historical_returns, (1 - confidence_level) * 100))
        #I could've used np.abs, no diff, it's just that obv, hid_VaR is negative, so I just negated it to make it positive.
        return historical_VaR

    def historical_cvar(self, confidence_level: float = 0.99) -> float:
        var = self.historical_returns[self.historical_returns <= -self.historical_var(confidence_level)]
        CVaR = -np.mean(var)
        return CVaR

    def parametric_var(self, current_volatility: float, confidence_level: float = 0.99) -> float:
        z_score = norm.ppf(1-confidence_level)
        parametric_VaR = -z_score * current_volatility

        return parametric_VaR

