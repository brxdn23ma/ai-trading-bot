"""
Custom exceptions for the Market Data Engine.

Defining project-specific exceptions improves readability,
error handling, and debugging throughout the application.
"""


class MarketDataError(Exception):
    """Base exception for all market data related errors."""


class InvalidTickerError(MarketDataError):
    """Raised when the provided ticker symbol is invalid."""


class InvalidDateError(MarketDataError):
    """Raised when a provided date is invalid or incorrectly formatted."""


class InvalidDateRangeError(MarketDataError):
    """Raised when the start date occurs after the end date."""


class EmptyDataError(MarketDataError):
    """Raised when the downloaded dataset is empty."""


class CacheError(MarketDataError):
    """Raised when reading from or writing to the cache fails."""