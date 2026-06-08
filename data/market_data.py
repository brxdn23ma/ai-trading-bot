import yfinance as yf


def get_price_data(ticker):

    data = yf.download(
        ticker,
        period="1y",
        interval="1d",
        auto_adjust=True
    )

    data.columns = data.columns.droplevel(1)

    return data