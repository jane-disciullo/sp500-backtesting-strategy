import numpy as np


def run_backtest(price, starting_balance=100_000):
    """
    Run the moving-average strategy backtest.

    Parameters:
        price (pandas.DataFrame): Price data containing
            'Long' and 'Return' columns.
        starting_balance (float): Initial portfolio balance.

    Returns:
        pandas.DataFrame: Price data with strategy returns
        and strategy balance.
    """

    price = price.copy()

price["Sys_Ret"] = np.where(
    price["Long"].shift(1) == True,
    1 + price["Return"],
    1
)

    price["Sys_Bal"] = (
        starting_balance * price["Sys_Ret"].cumprod()
    )

    return price
