"""Main trading loop placeholder."""
from __future__ import annotations

import time
from typing import Iterable

from src.binance_client import BinanceClient
from src.config import get_settings
from src.execution import ExecutionEngine
from src.features import RuntimeFeatureBuilder
from src.models import ModelInference
from src.signals import Signal, SignalStore


def run_trading_service(poll_interval: float = 1.0) -> None:
    """
    Run the main trading service loop.

    This is a placeholder implementation that wires components together.
    """
    settings = get_settings()
    client = BinanceClient()
    feature_builder = RuntimeFeatureBuilder()
    inference = ModelInference()
    executor = ExecutionEngine()
    signal_store = SignalStore()

    symbols: Iterable[str] = settings.symbols

    while True:
        # Placeholder: fetch latest candle(s), update features, and compute signals.
        for symbol in symbols:
            _ = symbol
            # In a real implementation, we'd ingest new candles and compute features.
            # signal_data = inference.predict(features)
            # signal = Signal(symbol=symbol, action=signal_data["action"], confidence=signal_data["confidence"])
            # signal_store.set(signal)
            # executor.execute_signal(symbol, signal_data)
        time.sleep(poll_interval)


if __name__ == "__main__":
    run_trading_service()

