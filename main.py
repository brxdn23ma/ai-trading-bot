from backtest.backtester import run_backtest

from backtest.performance import (
    calculate_total_return,
    calculate_annual_return,
    calculate_volatility,
    calculate_sharpe_ratio,
    calculate_max_drawdown
)

data = run_backtest("AAPL")

print()

print(
    "Total Return:",
    round(
        calculate_total_return(data) * 100,
        2
    ),
    "%"
)

print(
    "Annual Return:",
    round(
        calculate_annual_return(data) * 100,
        2
    ),
    "%"
)

print(
    "Volatility:",
    round(
        calculate_volatility(data) * 100,
        2
    ),
    "%"
)

print(
    "Sharpe Ratio:",
    round(
        calculate_sharpe_ratio(data),
        2
    )
)

print(
    "Max Drawdown:",
    round(
        calculate_max_drawdown(data) * 100,
        2
    ),
    "%"
)


print(
    data[
        [
            "Close",
            "MA20",
            "MA50",
            "Signal",
            "Position"
        ]
    ].tail(20)
)