import numpy as np


def calculate_total_return(price, starting_balance=100_000):
    """Calculate final value and total return for the benchmark and strategy."""

    final_bench = price["Bench_Bal"].iloc[-1]
    final_strategy = price["Sys_Bal"].iloc[-1]

    bench_total_return = (final_bench / starting_balance) - 1
    sys_total_return = (final_strategy / starting_balance) - 1

    return {
        "final_bench": final_bench,
        "final_strategy": final_strategy,
        "bench_total_return": bench_total_return,
        "sys_total_return": sys_total_return,
    }


def calculate_sharpe_ratio(price, risk_free_rate=0):
    """Calculate annualized Sharpe ratios for the benchmark and strategy."""

    strategy_daily_returns = price["Sys_Ret"] - 1

    bench_sharpe = (
        (price["Daily_Return"].mean() - risk_free_rate)
        / price["Daily_Return"].std()
    ) * np.sqrt(252)

    strategy_sharpe = (
        (strategy_daily_returns.mean() - risk_free_rate)
        / strategy_daily_returns.std()
    ) * np.sqrt(252)

    return {
        "bench_sharpe": bench_sharpe,
        "strategy_sharpe": strategy_sharpe,
    }


def calculate_cagr(price, years):
    """Calculate CAGR for the benchmark and strategy."""

    cagr_bench = (
        (price["Bench_Bal"].iloc[-1] / price["Bench_Bal"].iloc[0])
        ** (1 / years)
    ) - 1

    cagr_strategy = (
        (price["Sys_Bal"].iloc[-1] / price["Sys_Bal"].iloc[0])
        ** (1 / years)
    ) - 1

    return {
        "cagr_bench": cagr_bench,
        "cagr_strategy": cagr_strategy,
    }


def calculate_max_drawdown(price):
    """Calculate maximum drawdown for the benchmark and strategy."""

    price = price.copy()

    price["Bench_Peak"] = price["Bench_Bal"].cummax()
    price["Bench_DD"] = price["Bench_Bal"] - price["Bench_Peak"]

    price["Sys_Peak"] = price["Sys_Bal"].cummax()
    price["Sys_DD"] = price["Sys_Bal"] - price["Sys_Peak"]

    dd_bench = (
        (price["Bench_DD"] / price["Bench_Peak"]).min()
    ) * 100

    dd_strategy = (
        (price["Sys_DD"] / price["Sys_Peak"]).min()
    ) * 100

    return {
        "dd_bench": dd_bench,
        "dd_strategy": dd_strategy,
    }
