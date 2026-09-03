import numpy as np

class VolatilityModel:
    def __init__(self, historical_returns: np.ndarray):
        # The model only takes in raw numbers. No internet fetching here.
        self.returns = np.asarray(historical_returns)

    def ewma_variance(self, lambda_: float = 0.94) -> np.ndarray:
        arr1 = np.zeros(len(self.returns))
        arr1[0] = np.var(self.returns)
        for i in range(1, len(self.returns)):
            arr1[i] = lambda_ * arr1[i-1] + (1-lambda_)*(self.returns[i-1]**2)

        return arr1


        