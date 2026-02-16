from __future__ import annotations

from app.core.config import settings
from app.schemas.ai import AIInsightRequest
from app.services.calculations import allocation_percent_by_risk, confidence_band


class AIInsightService:
    def generate(self, payload: AIInsightRequest) -> dict:
        metrics = payload.metrics
        pe = metrics.get("pe_ttm", 0)
        industry_pe = metrics.get("industry_pe", pe)
        debt_eq = metrics.get("debt_equity", 0.5)
        volatility = metrics.get("volatility_grade", "medium")

        score = 60
        if pe < industry_pe:
            score += 6
        if debt_eq > 1:
            score -= 5

        alloc_pct = allocation_percent_by_risk(payload.user_profile.risk_tolerance, str(volatility))
        alloc_pct = min(alloc_pct, payload.user_profile.max_stock_allocation_pct)
        alloc_amt = round(payload.user_profile.investable_amount * alloc_pct / 100, 2)

        return {
            "summary": f"{payload.symbol} shows mixed signals with valuation and leverage balance requiring close monitoring.",
            "pros": [
                f"Valuation check: P/E {pe} vs industry {industry_pe} used in assessment.",
                "Cashflow conversion remains supportive for reinvestment.",
                "Technical trend does not show major breakdown currently.",
            ],
            "cons": [
                f"Debt/Equity at {debt_eq} can pressure downside during weak cycles.",
                "Earnings sensitivity to sector demand remains a risk.",
                "Macro rate volatility may compress multiples.",
            ],
            "valuation_view": "Fair to slightly expensive unless growth re-accelerates.",
            "technical_view": "Neutral-to-bullish with confirmation needed above resistance.",
            "sector_outlook": "Sector has structural demand tailwinds but regulation and competition are key risks.",
            "allocation_suggestion": {"percent": alloc_pct, "amount": alloc_amt},
            "sell_triggers": [
                "Breakdown below key 200DMA with volume expansion.",
                "Two consecutive quarters of margin deterioration.",
                "Debt/Equity rising above prior 3Y average by >20%.",
            ],
            "alternatives": ["MSFT", "GOOGL", "TCS.NS"],
            "confidence_range": confidence_band(score),
            "assumptions": [
                "No severe macro shock in next 12 months.",
                "Revenue growth remains within recent 3Y range.",
            ],
            "disclaimer": settings.disclaimer,
        }
