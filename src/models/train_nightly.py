"""Nightly retraining entrypoint placeholder."""
from __future__ import annotations

from src.config import get_settings


def train_nightly() -> None:
    """Retrain the model on the most recent data and update artifacts."""
    _ = get_settings()
    raise NotImplementedError("Nightly training is not implemented yet.")


if __name__ == "__main__":
    train_nightly()

