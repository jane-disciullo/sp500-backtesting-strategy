## sp500-signal-research
Python-based quantitative research on systematic trading signals applied to the S&P 500. This project evaluates a 200-day moving average strategy against a Buy & Hold benchmark and investigates parameter sensitivity, out-of-sample performance, risk, transaction costs, and market regimes.

## Tools
- Python
- Pandas
- NumPy
- Matplotlib
- yfinance
- Jupyter Notebook

## Strategy
The baseline strategy uses the 200-day MA to determine whether to remain invested in SPY or move to cash.
The project also tests different MA parameters, evaluating how signal performance changes across different market conditions.

## Research
The research process includes:
Baseline backtesting
Moving-average parameter testing
Strategy comparison
Out-of-sample testing
Risk and performance analysis
Transaction-cost analysis
Market-regime analysis

## Limitations
The backtest does not fully account for taxes, market impact, liquidity constraints, or other real-world execution considerations. Historical backtest results do not guarantee future performance.
