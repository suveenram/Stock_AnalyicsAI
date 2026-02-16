from __future__ import annotations

from typing import Any

from app.data.mock_data import STOCKS
from app.providers.interfaces import FundamentalsProvider, MarketDataProvider, NewsProvider


class MockMarketDataProvider(MarketDataProvider):
    def search(self, query: str) -> list[dict[str, Any]]:
        q = query.lower()
        out = []
        for item in STOCKS.values():
            if q in item["symbol"].lower() or q in item["company_name"].lower():
                out.append(
                    {
                        "symbol": item["symbol"],
                        "exchange": item["exchange"],
                        "name": item["company_name"],
                        "isin": "N/A",
                    }
                )
        return out

    def get_overview(self, symbol: str) -> dict[str, Any] | None:
        return STOCKS.get(symbol.upper()) or STOCKS.get(symbol)

    def get_technicals(self, symbol: str) -> dict[str, Any] | None:
        stock = STOCKS.get(symbol.upper()) or STOCKS.get(symbol)
        return stock.get("technical") if stock else None


class MockFundamentalsProvider(FundamentalsProvider):
    def get_fundamentals(self, symbol: str) -> dict[str, Any]:
        stock = STOCKS.get(symbol.upper()) or STOCKS.get(symbol)
        if not stock:
            return {}
        metrics = stock["key_metrics"]
        return {
            "symbol": stock["symbol"],
            "profitability": {"gross_margin": 41.2, "operating_margin": 30.1, "net_margin": 24.3},
            "growth": {"revenue_cagr_3y": 0.081, "eps_cagr_3y": 0.102, "fcf_cagr_3y": 0.074},
            "returns": {"roe": metrics.get("roe", 12.0), "roic": 18.4, "roa": 11.1},
            "health": {"debt_equity": metrics.get("debt_equity", 0.5), "current_ratio": 1.22, "interest_coverage": 17.2},
            "cashflow": {"fcf_margin": 0.19, "fcf_conversion": 1.08},
            "red_flags": ["Receivables growth above revenue in latest quarter"],
            "history": [{"year": y, "revenue": 100 + y * 4, "eps": 2.1 + y * 0.09} for y in range(2015, 2025)],
        }


class MockNewsProvider(NewsProvider):
    def get_news(self, symbol: str) -> list[dict[str, Any]]:
        return [
            {
                "headline": f"{symbol} expands product portfolio",
                "sentiment": "positive",
                "source": "MockWire",
                "url": "https://example.com/news-1",
            }
        ]
