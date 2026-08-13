def generate_ma_signal(price, ma=200):
    """
    Calculate a moving average and generate a long signal.

    Parameters:
        price (pandas.DataFrame): Historical price data.
        ma (int): Moving-average window.

    Returns:
        pandas.DataFrame: Price data with MA and Long columns.
    """

    price = price.copy()

    price["MA"] = price["Close"].rolling(window=ma).mean()

    price["Long"] = price["Close"] > price["MA"]

    return price


def generate_momentum_signal(price, lookback=20):
    """
    Generate a momentum signal based on past price.

    Parameters:
        price (pandas.DataFrame): Historical price data.
        lookback (int): Number of trading days used for the momentum signal.

    Returns:
        pandas.DataFrame: Price data with Momentum and Long columns.
    """

    price = price.copy()

    price["Momentum"] = (
        price["Close"] / price["Close"].shift(lookback) - 1
    )

    price["Long"] = price["Momentum"] > 0

    return price
