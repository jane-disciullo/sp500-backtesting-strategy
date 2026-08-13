from datetime import datetime

from src.data import load_spy_data
from src.signals import generate_momentum_signal
from src.backtest import run_backtest
from src.metrics import (
    calculate_total_return,
    calculate_sharpe_ratio,
    calculate_cagr,
    calculate_max_drawdown,
)


def run_momentum_experiment(
    lookback=20,
    starting_balance=100_000,
    start=datetime(2015, 1, 1),
    end=datetime(2026, 1, 1),
):
    """
    Run a momentum strategy experiment on SPY.

    Parameters
    ----------
    lookback : int, default=20
        Number of trading days used to measure momentum.
    starting_balance : float, default=100000
        Initial portfolio balance.
    start : datetime
        Start date for the backtest.
    end : datetime
        End date for the backtest.

    Returns
    -------
    dict
        Backtest data and performance metrics.
    """

    # Load SPY data
    price = load_spy_data(
        start=start,
        end=end,
    )

    # Generate momentum signal
    price = generate_momentum_signal(
        price,
        lookback=lookback,
    )

    # Run strategy backtest
    price = run_backtest(
        price,
        starting_balance=starting_balance,
    )

    # Calculate performance metrics
    total_return = calculate_total_return(
        price,
        starting_balance=starting_balance,
    )

    sharpe = calculate_sharpe_ratio(price)

    years = (price.index.max() - price.index.min()).days / 365.25

    cagr = calculate_cagr(
    price,
    years=years,
    starting_balance=starting_balance,
)

    drawdown = calculate_max_drawdown(price)

    return {
        "price": price,
        "lookback": lookback,
        "total_return": total_return,
        "sharpe": sharpe,
        "cagr": cagr,
        "drawdown": drawdown,
    }
