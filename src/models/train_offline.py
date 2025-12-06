"""One-time offline training script placeholder."""
from __future__ import annotations

from src.config import get_settings


def train_offline() -> None:
    """Build dataset, train initial model, and persist artifacts."""
    # Implement data loading, feature building, and model training here.
    _ = get_settings()
    raise NotImplementedError("Offline training is not implemented yet.")


if __name__ == "__main__":
    train_offline()

