from datetime import datetime

from src.data import load_spy_data
from src.signals import generate_ma_signal
from src.backtest import run_backtest
from src.metrics import (
    calculate_total_return,
    calculate_sharpe_ratio,
    calculate_cagr,
    calculate_max_drawdown,
)


def run_moving_average_experiment(
    ma=200,
    starting_balance=100_000,
    start=datetime(2015, 1, 1),
    end=datetime(2026, 1, 1),
):
    """
    Run a moving-average strategy experiment on SPY.

    Parameters
    ----------
    ma : int, default=200
        Moving-average window.
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

    # Generate moving-average signal
    price = generate_ma_signal(
        price,
        ma=ma,
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
        "ma": ma,
        "total_return": total_return,
        "sharpe": sharpe,
        "cagr": cagr,
        "drawdown": drawdown,
    }
