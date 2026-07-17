"""
Caching utilities for the Market Data Engine.

This module provides a local file-based cache for downloaded market
data using the Apache Parquet format.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from research.data.exceptions import CacheError
from research.data.validator import ValidatedRequest


class CacheManager:
    """
    Handles reading and writing cached market datasets.
    """

    def __init__(self, cache_dir: str | Path = "data/cache") -> None:
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def get_cache_path(
        self,
        request: ValidatedRequest,
    ) -> Path:
        """
        Build a unique cache filename from a validated request.
        """
        filename = (
            f"{request.ticker}_"
            f"{request.start_date.isoformat()}_"
            f"{request.end_date.isoformat()}.parquet"
        )

        return self.cache_dir / filename

    def exists(
        self,
        request: ValidatedRequest,
    ) -> bool:
        """
        Return True if the requested dataset exists in cache.
        """
        return self.get_cache_path(request).exists()

    def load(
        self,
        request: ValidatedRequest,
    ) -> pd.DataFrame:
        """
        Load a cached dataset.
        """
        path = self.get_cache_path(request)

        try:
            return pd.read_parquet(path)
        except Exception as exc:
            raise CacheError(
                f"Failed to load cache: {path}"
            ) from exc

    def save(
        self,
        request: ValidatedRequest,
        dataframe: pd.DataFrame,
    ) -> None:
        """
        Save a DataFrame to the cache.
        """
        path = self.get_cache_path(request)

        try:
            dataframe.to_parquet(path, index=True)
        except Exception as exc:
            raise CacheError(
                f"Failed to save cache: {path}"
            ) from exc