"""Configuration loader for the Binance futures trading bot."""
from __future__ import annotations

from functools import lru_cache
from typing import List

from dotenv import load_dotenv
from pydantic import BaseSettings, Field, validator


# Load environment variables from a local .env file if present.
load_dotenv()


class Settings(BaseSettings):
    """Application settings read from environment variables."""

    binance_api_key: str | None = Field(default=None, env="BINANCE_API_KEY")
    binance_api_secret: str | None = Field(default=None, env="BINANCE_API_SECRET")
    binance_env: str = Field(default="testnet", env="BINANCE_ENV")
    trading_enabled: bool = Field(default=False, env="TRADING_ENABLED")
    symbols: List[str] = Field(default_factory=lambda: ["BTCUSDT"], env="SYMBOLS")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

    @validator("binance_env")
    def validate_env(cls, value: str) -> str:
        allowed = {"testnet", "mainnet"}
        if value not in allowed:
            raise ValueError(f"BINANCE_ENV must be one of {allowed}")
        return value

    @validator("symbols", pre=True)
    def split_symbols(cls, value) -> List[str]:
        if value is None:
            return ["BTCUSDT"]
        if isinstance(value, str):
            parsed = [item.strip().upper() for item in value.split(",") if item.strip()]
            return parsed or ["BTCUSDT"]
        return value

    @property
    def is_live_trading(self) -> bool:
        """True when trading should reach the real exchange."""
        return self.trading_enabled and self.binance_env == "mainnet"


@lru_cache()
def get_settings() -> Settings:
    """Return cached settings instance."""
    return Settings()


__all__ = ["Settings", "get_settings"]

