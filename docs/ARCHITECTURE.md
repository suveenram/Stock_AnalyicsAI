# System Architecture

## Stack Choice
- Frontend: Next.js (App Router) + TypeScript + Tailwind.
- Backend: FastAPI (Python) with clean layering.
- Database: PostgreSQL.
- Cache: Redis.
- Jobs: Celery-compatible scheduled refresh placeholder.
- Auth: JWT email/password + Google OAuth placeholder hooks.

## High-Level Flow
1. Data ingestion adapters pull market/fundamental/news data.
2. Normalization pipeline converts provider payloads into canonical models.
3. Storage layer persists OHLCV, financial statements, ratios, events, ownership snapshots.
4. Metric engine computes valuation bands, CAGR, technical indicators, risk metrics.
5. API layer serves stock pages, compare, AI insights, portfolio, glossary.
6. Frontend renders tabbed UX with Beginner/Pro modes and export options.

## Clean Architecture
- `api/`: route controllers.
- `services/`: business logic.
- `repositories/`: data access abstraction.
- `providers/`: pluggable market/fundamental/news adapters.
- `schemas/`: request/response contracts.
- `core/`: config, security, logging.

## Provider Interfaces
- `MarketDataProvider`: search, quote, ohlcv, events.
- `FundamentalsProvider`: profile, statements, ratios, ownership.
- `NewsProvider`: headlines, sentiment.

Adapters can be swapped by config (`provider_mode=mock|live`).

## Data Pipeline
`ingestion -> normalization -> storage -> computed metrics -> api cache`

## Observability & Security
- Structured request logging middleware.
- `/health` endpoint with DB/Redis quick checks.
- Input validation via Pydantic.
- Rate-limit middleware placeholder.
- Auth guards for portfolio endpoints.

## Performance
- Redis caching on stock detail and indicator endpoints.
- Precompute daily ratios + technicals via scheduled job.
- DB indexes on symbol/date/exchange.

## Beginner/Pro Mode
- `ui_mode` in user preferences.
- Beginner: condensed cards and simplified copy.
- Pro: full statements/raw tables/advanced indicators/export toggles.
