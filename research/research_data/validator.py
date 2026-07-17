"""
Input validation utilities for the Market Data Engine.

This module validates user inputs before any network requests
or data processing are performed.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True, slots=True)
class ValidatedRequest:
    ticker: str
    start_date: date
    end_date: date

from dateutil.parser import ParserError, parse

from research.research_data.exceptions import (
    InvalidDateError,
    InvalidDateRangeError,
    InvalidTickerError,
)


class InputValidator:
    """Utility class for validating Market Data Engine inputs."""

    @staticmethod
    def validate_ticker(ticker: str) -> str:
        """
        Validate a ticker symbol.

        Parameters
        ----------
        ticker : str
            Asset ticker provided by the user.

        Returns
        -------
        str
            Uppercase, stripped ticker.

        Raises
        ------
        InvalidTickerError
            If the ticker is empty or invalid.
        """
        if not isinstance(ticker, str):
            raise InvalidTickerError("Ticker must be a string.")

        ticker = ticker.strip().upper()

        if not ticker:
            raise InvalidTickerError("Ticker cannot be empty.")

        return ticker

    @staticmethod
    def validate_dates(
        start_date: str,
        end_date: str,
    ) -> Tuple[date, date]:
        """
        Validate and parse start/end dates.

        Parameters
        ----------
        start_date : str
        end_date : str

        Returns
        -------
        tuple[date, date]

        Raises
        ------
        InvalidDateError
        InvalidDateRangeError
        """
        try:
            start = parse(start_date).date()
            end = parse(end_date).date()
        except (ParserError, TypeError):
            raise InvalidDateError(
                "Dates must be valid and in YYYY-MM-DD format."
            ) from None

        if start > end:
            raise InvalidDateRangeError(
                "Start date cannot be later than end date."
            )

        return start, end

@classmethod
def validate(
    cls,
    ticker: str,
    start_date: str,
    end_date: str,
) -> ValidatedRequest:
    """
    Validate all inputs.
    """
    ticker = cls.validate_ticker(ticker)
    start, end = cls.validate_dates(start_date, end_date)

    return ValidatedRequest(
        ticker=ticker,
        start_date=start,
        end_date=end,
    )