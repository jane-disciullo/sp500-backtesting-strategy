import yfinance as yf


def load_spy_data(
    start="2015-01-01",
    end="2026-01-01",
    interval="1d"
):
    """
    Download historical SPY price data.
    """

    price = yf.download(
        tickers="SPY",
        start=start,
        end=end,
        interval=interval,
        multi_level_index=False
    )

    return price