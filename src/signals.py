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
