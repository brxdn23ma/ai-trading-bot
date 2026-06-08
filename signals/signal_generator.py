from data.market_data import get_price_data
from strategy.moving_average import (
    calculate_moving_averages,
    generate_signal
)


def generate_signal(data):

    latest = data.iloc[-1]

    ma20 = latest["MA20"]
    ma50 = latest["MA50"]

    close = latest["Close"]

    if ma20 > ma50:
        return "BUY"

    elif ma20 < ma50:
        return "SELL"

    return "HOLD"


def generate_signals(watchlist):

    signals = {}

    for ticker in watchlist:

        data = get_price_data(ticker)

        data = calculate_moving_averages(data)

        signal = generate_signal(data)

        signals[ticker] = signal

    return signals