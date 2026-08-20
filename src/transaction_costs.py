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
        Transaction cost per trade, expressed as a decimal.
        Example: 0.0002 = 2 basis points.
    starting_balance : float, default=100000
        Initial portfolio balance.

    Returns
    -------
    pd.DataFrame
        DataFrame containing:
        - Trade: whether a position change occurred
        - Sys_Ret_Cost: strategy return after transaction costs
        - Sys_Bal_Cost: portfolio balance after transaction costs
    """

    price = price.copy()

    # Validate required columns
    required_columns = {"Long", "Sys_Ret"}
    missing_columns = required_columns - set(price.columns)

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}"
        )

    # Validate inputs
    if transaction_cost < 0:
        raise ValueError("transaction_cost must be non-negative")

    if transaction_cost >= 1:
        raise ValueError("transaction_cost must be less than 1")

    if starting_balance <= 0:
        raise ValueError("starting_balance must be positive")

    if price.empty:
        raise ValueError("price DataFrame cannot be empty")

    # Identify when the strategy changes position
    price["Trade"] = price["Long"].ne(price["Long"].shift(1))

    # Do not count the first observation as a trade
    price.loc[price.index[0], "Trade"] = False

    # Apply transaction cost when a trade occurs
    price["Sys_Ret_Cost"] = np.where(
        price["Trade"],
        price["Sys_Ret"] * (1 - transaction_cost),
        price["Sys_Ret"],
    )

    # Calculate portfolio balance after transaction costs
    price["Sys_Bal_Cost"] = (
        starting_balance * price["Sys_Ret_Cost"].cumprod()
    )

    return price
