from __future__ import annotations

from app.core.config import settings
from app.providers.mock_provider import (
    MockFundamentalsProvider,
    MockMarketDataProvider,
    MockNewsProvider,
)


class StockService:
    def __init__(self) -> None:
        self.market = MockMarketDataProvider()
        self.fundamentals = MockFundamentalsProvider()
        self.news = MockNewsProvider()

    def search(self, query: str) -> dict:
        return {"results": self.market.search(query), "recent": ["AAPL", "RELIANCE.NS"]}

    def overview(self, symbol: str) -> dict:
        data = self.market.get_overview(symbol)
        if not data:
            return {}
        return {
            "symbol": data["symbol"],
            "exchange": data["exchange"],
            "company_name": data["company_name"],
            "sector": data["sector"],
            "industry": data["industry"],
            "quote": data["quote"],
            "key_metrics": data["key_metrics"],
            "disclaimer": settings.disclaimer,
        }

    def fundamentals_view(self, symbol: str) -> dict:
        return self.fundamentals.get_fundamentals(symbol)

    def technical_view(self, symbol: str) -> dict:
        tech = self.market.get_technicals(symbol)
        return {"symbol": symbol, **tech} if tech else {}

    def news_view(self, symbol: str) -> dict:
        return {"symbol": symbol, "items": self.news.get_news(symbol)}

    def compare(self, symbols: list[str]) -> dict:
        rows = []
        for sym in symbols[:4]:
            ov = self.overview(sym)
            tech = self.technical_view(sym)
            if ov:
                rows.append(
                    {
                        "symbol": sym,
                        "pe_ttm": ov["key_metrics"].get("pe_ttm"),
                        "roe": ov["key_metrics"].get("roe"),
                        "debt_equity": ov["key_metrics"].get("debt_equity"),
                        "trend": tech.get("trend", "unknown"),
                    }
                )
        return {"symbols": symbols[:4], "rows": rows}
