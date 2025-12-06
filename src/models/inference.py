"""Model inference utilities."""
from __future__ import annotations

from pathlib import Path
from typing import Any, Dict


class ModelInference:
    """Load the latest model and produce trading decisions."""

    def __init__(self, model_path: str | Path = "models/model_latest.pkl") -> None:
        self.model_path = Path(model_path)
        # Placeholder: model loading logic will be added later.
        self.model = None

    def predict(self, features) -> Dict[str, Any]:
        """
        Produce a prediction using the loaded model.
        Expected output: dict with keys like 'action' (LONG/SHORT/HOLD) and 'confidence'.
        """
        raise NotImplementedError("Model inference is not implemented yet.")

