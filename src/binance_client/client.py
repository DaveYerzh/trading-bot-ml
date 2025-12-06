"""Lightweight Binance Futures client wrapper (HTTP/WebSocket stubs)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from src.config import get_settings


@dataclass
class BinanceClient:
    """Placeholder Binance client to be implemented with real HTTP/WebSocket calls."""

    api_key: Optional[str] = None
    api_secret: Optional[str] = None
    use_testnet: bool = True

    def __post_init__(self) -> None:
        settings = get_settings()
        self.api_key = self.api_key or settings.binance_api_key
        self.api_secret = self.api_secret or settings.binance_api_secret
        self.use_testnet = settings.binance_env == "testnet"

    def get_klines(self, symbol: str, interval: str, limit: int = 500) -> List[Dict[str, Any]]:
        """Fetch historical klines. To be implemented with Binance REST API."""
        raise NotImplementedError("get_klines is not implemented yet.")

    def get_open_interest(self, symbol: str) -> Dict[str, Any]:
        """Fetch open interest for a symbol."""
        raise NotImplementedError("get_open_interest is not implemented yet.")

    def get_funding_rates(self, symbol: str, limit: int = 100) -> List[Dict[str, Any]]:
        """Fetch funding rate history."""
        raise NotImplementedError("get_funding_rates is not implemented yet.")

    def place_order(self, symbol: str, side: str, quantity: float, position_side: str | None = None) -> Dict[str, Any]:
        """Place an order if trading is enabled; otherwise raise or log."""
        settings = get_settings()
        if not settings.trading_enabled:
            raise RuntimeError("Trading is disabled (TRADING_ENABLED=false).")
        raise NotImplementedError("place_order is not implemented yet.")

    def cancel_order(self, symbol: str, order_id: str) -> Dict[str, Any]:
        """Cancel an order."""
        raise NotImplementedError("cancel_order is not implemented yet.")

