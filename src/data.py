import yfinance as yf


def load_spy_data(
    start="2015-01-01",
    end="2026-01-01",
    interval="1d"
):
    """
    Download historical SPY price data and calculate return columns.

    Returns
    -------
    pandas.DataFrame
        SPY price data with daily returns, return multipliers,
        and benchmark portfolio value.
    """

    price = yf.download(
        tickers="SPY",
        start=start,
        end=end,
        interval=interval,
        multi_level_index=False
    )

    # Daily simple return
    price["Daily_Return"] = price["Close"].pct_change()

    # Return multiplier used by the backtest
    price["Return"] = price["Close"] / price["Close"].shift(1)
    price.loc[price.index[0], "Return"] = 1

    # Benchmark portfolio value
    price["Bench_Bal"] = (
        100_000 * (1 + price["Daily_Return"]).cumprod()
    )

    return price
