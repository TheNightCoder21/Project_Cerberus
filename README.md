# Cerberus Quant: Market Risk & Tail Dynamics Engine

Cerberus Quant is a vectorized, from-scratch quantitative research framework designed to model non-Gaussian financial tail behavior and evaluate the empirical stability of standard risk metrics. 

Standard parametric models systematically underestimate the frequency and magnitude of market crashes by assuming a Gaussian distribution of log returns. This engine diagnoses those mathematical assumptions, implementing dynamic conditional volatility models and non-parametric risk measures to expose Look-Ahead Bias and Volatility Clustering in historical backtests.

## Core Capabilities
* **Empirical Distribution Analysis:** Vectorized calculation of time-series moments to isolate excess kurtosis (leptokurtic properties) and negative skewness in historical equity data.
* **Risk Metric Implementation:** Calculation of Value at Risk (VaR) and Conditional Expected Shortfall (CVaR) to quantify tail-risk magnitude beyond the quantile threshold.
* **Conditional Volatility Modeling:** A recursive Exponentially Weighted Moving Average (EWMA) engine to track dynamic market regimes and volatility clustering.
* **Out-of-Sample Backtesting:** A strictly isolated, rolling-window backtest architecture to empirically test theoretical hit rates against actual market breaches.

## Technical Architecture
* Written in pure Python, utilizing `numpy` for $O(N)$ vectorized array operations and `scipy.stats` for distribution metrics.
* Implements strict Separation of Concerns (SoC) between data ingestion, mathematical processing, and backtest execution.
* Environment and dependency management handled via `uv`.

## Quick Start
```bash
# Clone the repository
git clone [https://github.com/YourUsername/Project_Cerberus.git](https://github.com/YourUsername/Project_Cerberus.git)
cd Project_Cerberus

# Sync the virtual environment using uv
uv sync

# Run the comparative risk model backtest
uv run python -m src.cerberus_quant.experiments.h2_backtest
```

~IG
