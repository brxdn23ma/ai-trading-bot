def calculate_moving_averages(data):

    data["MA20"] = (
        data["Close"]
        .rolling(20)
        .mean()
    )

    data["MA50"] = (
        data["Close"]
        .rolling(50)
        .mean()
    )

    return data

def generate_signal(data):

    latest = data.iloc[-1]

    if latest["MA20"] > latest["MA50"]:
        return "BUY"

    elif latest["MA20"] < latest["MA50"]:
        return "SELL"

    return "HOLD"