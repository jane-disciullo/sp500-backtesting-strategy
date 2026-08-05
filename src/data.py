import yfinance as yf


def load_spy_data(
    start="2015-01-01",
    end="2026-01-01",
    interval="1d"
):
    """
    Download historical SPY price data and calculate returns.

    Returns:
        pandas.DataFrame: SPY price data with return columns.
    """

    price = yf.download(
        tickers="SPY",
        start=start,
        end=end,
        interval=interval,
        multi_level_index=False
    )

    # Daily simple return
    price["Return"] = price["Close"].pct_change()

    # Benchmark daily return
    price["Daily_Return"] = price["Return"]

    # Benchmark portfolio value
    price["Bench_Bal"] = 100_000 * (1 + price["Daily_Return"]).cumprod()

    return price
