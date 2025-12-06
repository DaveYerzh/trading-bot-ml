"""Position management placeholder."""
from __future__ import annotations

from typing import Dict


class PositionManager:
    """Cache and refresh current futures positions."""

    def __init__(self) -> None:
        self.positions: Dict[str, dict] = {}

    def refresh(self) -> Dict[str, dict]:
        """Fetch latest positions from the exchange."""
        raise NotImplementedError("Position refresh is not implemented yet.")

