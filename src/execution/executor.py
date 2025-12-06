"""Execution logic placeholder that respects risk and TRADING_ENABLED."""
from __future__ import annotations

from typing import Any, Dict

from src.config import get_settings


class ExecutionEngine:
    """Apply trading signals to live positions."""

    def __init__(self) -> None:
        self.settings = get_settings()

    def execute_signal(self, symbol: str, signal: Dict[str, Any]) -> None:
        """Execute a trading action if enabled."""
        if not self.settings.trading_enabled:
            # Only log in the real implementation; no live orders.
            return
        raise NotImplementedError("Execution logic is not implemented yet.")

