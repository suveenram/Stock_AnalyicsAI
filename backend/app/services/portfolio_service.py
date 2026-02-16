from __future__ import annotations


class PortfolioService:
    def summary(self) -> dict:
        return {
            "base_currency": "USD",
            "holdings": [
                {"symbol": "AAPL", "qty": 10, "avg_price": 180, "current_price": 215.3}
            ],
            "allocation": {"technology": 70, "cash": 30, "india": 0, "us": 100},
            "risk": {"beta": 1.05, "volatility": "medium", "max_drawdown": -0.18},
        }

    def recommendation(self) -> dict:
        return {
            "model": "Core-Satellite",
            "constraints": {"max_stock_pct": 10, "max_sector_pct": 30, "min_cash_pct": 5},
            "suggested_split": [
                {"bucket": "Core ETFs", "pct": 55},
                {"bucket": "Quality compounders", "pct": 30},
                {"bucket": "Satellite growth", "pct": 10},
                {"bucket": "Cash", "pct": 5},
            ],
        }
