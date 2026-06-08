from data.market_data import get_price_data
from strategy.moving_average import calculate_moving_averages


def generate_historical_signals(data):

    data["Signal"] = 0

    data.loc[
        data["MA20"] > data["MA50"],
        "Signal"
    ] = 1

    data.loc[
        data["MA20"] < data["MA50"],
        "Signal"
    ] = -1

    return data

# 1 = Long
# -1 = Out of market / Sell

def calculate_returns(data):

    data["Market_Return"] = (
        data["Close"]
        .pct_change()
    )

    return data

def calculate_strategy_returns(data):

    data["Strategy_Return"] = (
        data["Position"]
        .shift(1) # Shift the signal to align with the next day's return --> to prevent look-ahead bias
        * data["Market_Return"]
    )

    return data


def calculate_equity_curve(data):

    data["Equity"] = (
        1 + data["Strategy_Return"]
    ).cumprod()

    return data

def run_backtest(ticker):

    data = get_price_data(ticker)

    data = calculate_moving_averages(data)

    data = generate_trade_signals(data)

    data = generate_positions(data)

    data = calculate_returns(data)

    data = calculate_strategy_returns(data)

    data = calculate_equity_curve(data)

    return data


#################################
def generate_trade_signals(data):

    data["Signal"] = 0

    buy_condition = (
        (data["MA20"] > data["MA50"]) &
        (data["MA20"].shift(1) <= data["MA50"].shift(1))
    )

    sell_condition = (
        (data["MA20"] < data["MA50"]) &
        (data["MA20"].shift(1) >= data["MA50"].shift(1))
    )

    data.loc[buy_condition, "Signal"] = 1

    data.loc[sell_condition, "Signal"] = -1

    return data

def generate_positions(data):

    data["Position"] = (
        data["Signal"]
        .replace(-1, 0)
        .replace(1, 1)
        .ffill()
        .fillna(0)
    )

    return data