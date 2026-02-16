from pydantic import BaseModel


class UserProfile(BaseModel):
    risk_tolerance: str = "medium"
    max_stock_allocation_pct: float = 10
    investable_amount: float = 10000


class AIInsightRequest(BaseModel):
    symbol: str
    metrics: dict[str, float]
    user_profile: UserProfile


class AllocationSuggestion(BaseModel):
    percent: float
    amount: float


class AIInsightResponse(BaseModel):
    summary: str
    pros: list[str]
    cons: list[str]
    valuation_view: str
    technical_view: str
    sector_outlook: str
    allocation_suggestion: AllocationSuggestion
    sell_triggers: list[str]
    alternatives: list[str]
    confidence_range: str
    assumptions: list[str]
    disclaimer: str
