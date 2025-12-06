"""Offline feature builder for historical datasets."""
from __future__ import annotations

import pandas as pd


class OfflineFeatureBuilder:
    """Construct features from historical candle data for training."""

    def build(self, candles: pd.DataFrame) -> pd.DataFrame:
        """Return a dataframe with engineered features."""
        raise NotImplementedError("Offline feature builder is not implemented yet.")

