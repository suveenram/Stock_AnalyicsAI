from fastapi import APIRouter, HTTPException

from app.core.config import settings
from app.data.mock_data import GLOSSARY
from app.schemas.ai import AIInsightRequest, AIInsightResponse
from app.services.ai_service import AIInsightService
from app.services.stock_service import StockService
from app.services.portfolio_service import PortfolioService

router = APIRouter(prefix=settings.api_prefix)
stock_service = StockService()
ai_service = AIInsightService()
portfolio_service = PortfolioService()


@router.get("/health")
def health() -> dict:
    return {"status": "ok", "cache": "mock", "db": "mock"}


@router.get("/search")
def search(q: str) -> dict:
    return stock_service.search(q)


@router.get("/stocks/{symbol}/overview")
def overview(symbol: str) -> dict:
    data = stock_service.overview(symbol)
    if not data:
        raise HTTPException(status_code=404, detail="Symbol not found")
    return data


@router.get("/stocks/{symbol}/fundamentals")
def fundamentals(symbol: str) -> dict:
    return stock_service.fundamentals_view(symbol)


@router.get("/stocks/{symbol}/technicals")
def technicals(symbol: str) -> dict:
    return stock_service.technical_view(symbol)


@router.get("/stocks/{symbol}/news")
def news(symbol: str) -> dict:
    return stock_service.news_view(symbol)


@router.post("/compare")
def compare(payload: dict) -> dict:
    return stock_service.compare(payload.get("symbols", []))


@router.post("/ai/insight", response_model=AIInsightResponse)
def ai_insight(payload: AIInsightRequest) -> dict:
    return ai_service.generate(payload)


@router.get("/glossary/{key}")
def glossary(key: str) -> dict:
    term = GLOSSARY.get(key)
    if not term:
        raise HTTPException(status_code=404, detail="Glossary key not found")
    return term


@router.get("/stocks/{symbol}/financials")
def financials(symbol: str) -> dict:
    return {"symbol": symbol, "annual": stock_service.fundamentals_view(symbol).get("history", []), "quarterly": []}


@router.get("/stocks/{symbol}/valuation")
def valuation(symbol: str) -> dict:
    ov = stock_service.overview(symbol)
    if not ov:
        raise HTTPException(status_code=404, detail="Symbol not found")
    pe = ov["key_metrics"].get("pe_ttm", 0)
    return {
        "symbol": symbol,
        "current": {"pe_ttm": pe, "pb": ov["key_metrics"].get("pb")},
        "industry_median": {"pe_ttm": 20},
        "band_5y": {"cheap_below": 18, "normal": "18-27", "expensive_above": 27},
        "dcf": {"view": "fair", "assumptions": {"growth": 0.08, "wacc": 0.11, "terminal": 0.04}},
        "sensitivity": [["wacc/g", "3%", "4%"], ["10%", 250, 270], ["11%", 220, 238]],
    }


@router.get("/stocks/{symbol}/peers")
def peers(symbol: str) -> dict:
    return {"symbol": symbol, "peers": ["AAPL", "MSFT", "GOOGL", "AMZN", "META"]}


@router.get("/stocks/{symbol}/events")
def events(symbol: str) -> dict:
    return {"symbol": symbol, "items": [{"type": "earnings", "date": "2026-02-15"}]}


@router.get("/stocks/{symbol}/ownership")
def ownership(symbol: str) -> dict:
    return {"symbol": symbol, "promoter": 50.3 if symbol.endswith('.NS') else None, "institutional": 62.1}


@router.get('/portfolio')
def portfolio() -> dict:
    return portfolio_service.summary()


@router.get('/portfolio/allocation-recommendation')
def portfolio_recommendation() -> dict:
    return portfolio_service.recommendation()


@router.get('/exports/stock-report/{symbol}.pdf')
def export_stock_report(symbol: str) -> dict:
    return {"message": f"PDF export queued for {symbol}"}


@router.get('/exports/fundamentals/{symbol}.xlsx')
def export_fundamentals(symbol: str) -> dict:
    return {"message": f"XLSX export queued for {symbol}"}


@router.get('/exports/portfolio-performance.csv')
def export_portfolio() -> dict:
    return {"message": "CSV export queued"}
