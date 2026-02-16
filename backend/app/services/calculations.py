from __future__ import annotations

from math import isnan


def cagr(start_value: float, end_value: float, years: int) -> float | None:
    if years <= 0 or start_value <= 0 or end_value <= 0:
        return None
    return (end_value / start_value) ** (1 / years) - 1


def valuation_percentile(current: float, history: list[float]) -> float | None:
    valid = sorted([x for x in history if x is not None and not isnan(x)])
    if not valid:
        return None
    less_or_equal = sum(1 for x in valid if x <= current)
    return round((less_or_equal / len(valid)) * 100, 2)


def allocation_percent_by_risk(risk_tolerance: str, volatility_grade: str) -> float:
    risk_map = {"low": 0.5, "medium": 0.75, "high": 1.0}
    vol_penalty = {"low": 1.0, "medium": 0.8, "high": 0.6}
    base = risk_map.get(risk_tolerance, 0.75)
    adjusted = base * vol_penalty.get(volatility_grade, 0.8)
    return round(min(10.0, max(2.0, adjusted * 10)), 2)


def confidence_band(score: float) -> str:
    low = max(35, int(score - 8))
    high = min(85, int(score + 8))
    return f"{low}-{high}%"
