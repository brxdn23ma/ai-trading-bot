import pytest

from research.research_data.exceptions import (
    InvalidDateError,
    InvalidDateRangeError,
    InvalidTickerError,
)
from research.research_data.validator import InputValidator


def test_validate_ticker_success():
    assert InputValidator.validate_ticker("aapl") == "AAPL"


def test_validate_ticker_strips_whitespace():
    assert InputValidator.validate_ticker("  spy  ") == "SPY"


def test_validate_empty_ticker():
    with pytest.raises(InvalidTickerError):
        InputValidator.validate_ticker("")


def test_validate_non_string_ticker():
    with pytest.raises(InvalidTickerError):
        InputValidator.validate_ticker(123)


def test_validate_dates_success():
    start, end = InputValidator.validate_dates(
        "2020-01-01",
        "2020-12-31",
    )

    assert start.year == 2020
    assert end.year == 2020


def test_invalid_date_format():
    with pytest.raises(InvalidDateError):
        InputValidator.validate_dates(
            "not-a-date",
            "2020-01-01",
        )


def test_invalid_date_range():
    with pytest.raises(InvalidDateRangeError):
        InputValidator.validate_dates(
            "2021-01-01",
            "2020-01-01",
        )


def test_validate_all():
    ticker, start, end = InputValidator.validate(
        "aapl",
        "2020-01-01",
        "2020-12-31",
    )

    assert ticker == "AAPL"
    assert start.year == 2020
    assert end.year == 2020