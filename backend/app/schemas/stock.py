from typing import Any
from pydantic import BaseModel


class SearchResult(BaseModel):
    symbol: str
    exchange: str
    name: str
    isin: str | None = None


class OverviewResponse(BaseModel):
    symbol: str
    exchange: str
    company_name: str
    sector: str
    industry: str
    quote: dict[str, Any]
    key_metrics: dict[str, float | str]
    disclaimer: str


class TechnicalResponse(BaseModel):
    symbol: str
    trend: str
    risk_grade: str
    support: float
    resistance: float
    indicators: dict[str, float]
    signals: list[str]


class CompareResponse(BaseModel):
    symbols: list[str]
    rows: list[dict[str, Any]]
