"""In-memory signal store placeholder."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Dict, Optional


@dataclass
class Signal:
    """Represents a trading signal for a single symbol."""

    symbol: str
    action: str  # LONG / SHORT / HOLD
    confidence: float
    created_at: datetime = field(default_factory=datetime.utcnow)
    ttl: timedelta = field(default=timedelta(minutes=5))

    def is_expired(self, now: Optional[datetime] = None) -> bool:
        now = now or datetime.utcnow()
        return now > self.created_at + self.ttl


class SignalStore:
    """Store and retrieve recent signals with expiration."""

    def __init__(self) -> None:
        self._signals: Dict[str, Signal] = {}

    def set(self, signal: Signal) -> None:
        self._signals[signal.symbol] = signal

    def get(self, symbol: str, now: Optional[datetime] = None) -> Optional[Signal]:
        signal = self._signals.get(symbol)
        if signal and signal.is_expired(now):
            self._signals.pop(symbol, None)
            return None
        return signal

