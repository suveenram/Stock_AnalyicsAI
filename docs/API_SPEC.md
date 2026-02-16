# API Specification (v1)

Base URL: `/api/v1`

## Auth
### POST `/auth/register`
Req: `{ "email": "a@b.com", "password": "...", "name": "User" }`
Res: `{ "access_token": "jwt", "user": {...} }`

### POST `/auth/login`
Req: `{ "email": "a@b.com", "password": "..." }`
Res: `{ "access_token": "jwt" }`

## Search
### GET `/search?q=relia`
Res:
```json
{
  "results": [
    {"symbol":"RELIANCE.NS","exchange":"NSE","name":"Reliance Industries","isin":"INE002A01018"}
  ],
  "recent": ["AAPL","TCS.NS"]
}
```

## Stock Detail
### GET `/stocks/{symbol}/overview`
Res includes profile, quote, market cap, EV, key ratios, disclaimer.

### GET `/stocks/{symbol}/fundamentals?period=annual&years=10`
Res includes profitability/growth/returns/health/cashflow metrics, red flags, timeseries.

### GET `/stocks/{symbol}/financials?period=annual`
Res includes income/balance/cashflow statements.

### GET `/stocks/{symbol}/valuation`
Res includes current ratios, historical 5Y bands, peer medians, DCF summary, sensitivity matrix.

### GET `/stocks/{symbol}/technicals?range=1y`
Res includes ohlcv, indicators (SMA/EMA/RSI/MACD/BB/ATR), support/resistance, signals.

### GET `/stocks/{symbol}/peers`
Res includes top peers and ranking by valuation/growth/quality.

### GET `/stocks/{symbol}/news`
Res includes tagged sentiment and summarized headlines.

### GET `/stocks/{symbol}/events`
Res includes earnings/dividends/splits timeline.

### GET `/stocks/{symbol}/ownership`
Res includes promoter/insider/institutional trend.

## AI Insight
### POST `/ai/insight`
Req:
```json
{
  "symbol":"AAPL",
  "metrics": {"pe_ttm":28,"industry_pe":18,"debt_equity":1.2},
  "user_profile": {"risk_tolerance":"medium","max_stock_allocation_pct":10}
}
```
Res:
```json
{
  "summary":"...",
  "pros":["..."],
  "cons":["..."],
  "valuation_view":"...",
  "technical_view":"...",
  "sector_outlook":"...",
  "allocation_suggestion":{"percent":6,"amount":600},
  "sell_triggers":["..."],
  "alternatives":["MSFT","GOOGL"],
  "confidence_range":"55-68%",
  "assumptions":["Revenue growth remains above 8%"]
}
```

## Compare
### POST `/compare`
Req: `{ "symbols": ["AAPL","MSFT","GOOGL","AMZN"] }`
Res: side-by-side fundamentals, valuation, technical summary.

## Portfolio
### GET `/portfolio`
### POST `/portfolio/holdings`
### DELETE `/portfolio/holdings/{holding_id}`
### GET `/portfolio/allocation-recommendation`

## Exports
### GET `/exports/stock-report/{symbol}.pdf`
### GET `/exports/fundamentals/{symbol}.xlsx`
### GET `/exports/portfolio-performance.csv`

## Glossary
### GET `/glossary/{key}`
Returns definition/formula/interpretation/ranges/common mistakes.

## Health
### GET `/health`
