# Stock Analytics AI — Product Requirements Document

## 1. Product Vision
Stock Analytics AI is a dual-market (India + US) investment research platform for beginner-to-intermediate retail investors that combines fundamentals, technicals, AI explainability, and portfolio allocation guidance in one compliant interface.

## 2. Suggested App Names (5)
1. DualMarket Lens
2. EquityCompass AI
3. RupeeDollar Research
4. InvestorPilot Pro
5. StockClarity 360

## 3. Target Users
- Beginner investors needing plain-English insights.
- Intermediate investors requiring deep financial and technical analysis.
- Users investing across NSE/BSE and NYSE/NASDAQ with INR/USD exposure.

## 4. Success Metrics
- Stock detail page first contentful load under 3s for cached requests.
- 7-day activation: users run at least one stock search + open AI card.
- Retention: weekly returning users by watchlist/portfolio engagement.
- Explainability trust score from in-app feedback.

## 5. Core Principles
- Educational only, never personalized investment advice.
- Explain every recommendation with cited metrics.
- Show uncertainty as confidence ranges and assumptions.
- Avoid absolute wording (no guaranteed returns language).

## 6. User Stories
### Search & Discovery
- As a user, I can search by ticker/company/ISIN so I can quickly find instruments across India/US.
- As a user, I can see autocomplete and recent searches to reduce typing effort.

### Stock Analysis
- As a user, I can open a tabbed stock page to analyze overview, fundamentals, financials, valuation, technicals, peers, news, AI insights, events, and ownership.
- As a user, I can hover glossary terms to understand metrics with formulas and interpretation.

### Decision Support
- As a user, I can view a decision card (Invest/Hold/Avoid/Watchlist) with confidence range, time horizon, and explicit assumptions.
- As a user, I can get allocation suggestions bounded by my risk profile and portfolio constraints.
- As a user, I can read sell/trim triggers and alternatives in the same sector.

### Portfolio
- As a user, I can add holdings and see exposure by sector/geography/market cap.
- As a user, I can receive core-satellite allocation recommendations and SIP splits.

### Modes
- As a user, I can switch Beginner Mode (simplified) and Pro Mode (full detail).

## 7. Scope by Iteration
### Iteration 1 (MVP)
- Auth, stock search, overview/fundamentals/technicals tabs, AI summary card, glossary tooltips.

### Iteration 2
- Valuation, peers, screener, watchlist, alerts, compare page.

### Iteration 3
- Portfolio analytics, allocation engine, sell triggers, alternatives, basic backtesting.

## 8. Compliance Requirements
- Persistent disclaimer banner and report footer: “Educational only, not investment advice.”
- Probability-based confidence display and model assumptions.
- Recommendation explainability references to computed metrics.
- Risk warning for high concentration and volatile assets.

## 9. Non-Functional Requirements
- Accessibility (ARIA labels, keyboard support, color contrast).
- Caching + pagination for performance.
- Observability (request logs, health, job status).
- Rate limiting and input validation.

## 10. Deliverables
- PRD, architecture, DB schema, API spec.
- Full codebase (Next.js + FastAPI), mock mode + seeded data.
- Unit tests for critical calculations.
- Dockerized deployment + env guide.
- Data accuracy & disclaimer page.
