import numpy as np


def calculate_total_return(data):

    return (
        data["Equity"].iloc[-1] - 1
    )

def calculate_annual_return(data):

    total_return = (
        data["Equity"].iloc[-1]
    )

    years = len(data) / 252

    annual_return = (
        total_return ** (1 / years)
    ) - 1

    return annual_return

def calculate_volatility(data):

    volatility = (
        data["Strategy_Return"]
        .std()
        * np.sqrt(252)
    )

    return volatility

risk_free_rate = 0.045 # 10-year US Treasury yield as of June 2026

def calculate_sharpe_ratio(data):

    annual_return = calculate_annual_return(data)

    volatility = calculate_volatility(data)

    if volatility == 0:
        return 0

    return annual_return / volatility

def calculate_max_drawdown(data): # **important for risk management**

    rolling_max = (
        data["Equity"]
        .cummax()
    )

    drawdown = (
        data["Equity"]
        / rolling_max
    ) - 1

    return drawdown.min()

