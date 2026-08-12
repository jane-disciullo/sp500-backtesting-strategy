import numpy as np
import pandas as pd


def apply_transaction_costs(
    price: pd.DataFrame,
    transaction_cost: float = 0.0002,
    starting_balance: float = 100_000,
) -> pd.DataFrame:
    """
    Apply transaction costs whenever the strategy changes position.

    Parameters
    ----------
    price : pd.DataFrame
        DataFrame containing 'Long' and 'Sys_Ret' columns.
    transaction_cost : float, default=0.0002
        Transaction cost per trade.
    starting_balance : float, default=100000
        Initial portfolio balance.

    Returns
    -------
    pd.DataFrame
        DataFrame with trade indicator, cost-adjusted returns,
        and cost-adjusted portfolio balance.
    """

    price = price.copy()

    price["Trade"] = price["Long"].ne(price["Long"].shift(1))

    price["Sys_Ret_Cost"] = np.where(
        price["Trade"],
        price["Sys_Ret"] * (1 - transaction_cost),
        price["Sys_Ret"],
    )

    price["Sys_Bal_Cost"] = (
        starting_balance * price["Sys_Ret_Cost"].cumprod()
    )

    return price
