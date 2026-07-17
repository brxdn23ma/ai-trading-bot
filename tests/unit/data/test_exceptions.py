from research.data.exceptions import (
    CacheError,
    EmptyDataError,
    InvalidDateError,
    InvalidDateRangeError,
    InvalidTickerError,
    MarketDataError,
)


def test_exception_inheritance():
    """All custom exceptions should inherit from MarketDataError."""

    assert issubclass(InvalidTickerError, MarketDataError)
    assert issubclass(InvalidDateError, MarketDataError)
    assert issubclass(InvalidDateRangeError, MarketDataError)
    assert issubclass(EmptyDataError, MarketDataError)
    assert issubclass(CacheError, MarketDataError)


def test_raise_invalid_ticker():
    """Custom exceptions should be raisable."""

    try:
        raise InvalidTickerError("Invalid ticker.")
    except InvalidTickerError as exc:
        assert str(exc) == "Invalid ticker."