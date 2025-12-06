"""Runtime feature builder for live candle updates."""
from __future__ import annotations

import pandas as pd


class RuntimeFeatureBuilder:
    """Incrementally update features as new candles arrive."""

    def update(self, candle: pd.Series) -> pd.Series:
        """Return updated feature values for the latest candle."""
        raise NotImplementedError("Runtime feature builder is not implemented yet.")

