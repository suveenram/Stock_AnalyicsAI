from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class MarketDataProvider(ABC):
    @abstractmethod
    def search(self, query: str) -> list[dict[str, Any]]: ...

    @abstractmethod
    def get_overview(self, symbol: str) -> dict[str, Any] | None: ...

    @abstractmethod
    def get_technicals(self, symbol: str) -> dict[str, Any] | None: ...


class FundamentalsProvider(ABC):
    @abstractmethod
    def get_fundamentals(self, symbol: str) -> dict[str, Any]: ...


class NewsProvider(ABC):
    @abstractmethod
    def get_news(self, symbol: str) -> list[dict[str, Any]]: ...
