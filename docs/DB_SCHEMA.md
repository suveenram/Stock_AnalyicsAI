# Database Schema

## Core Tables
### users
- id (uuid, pk)
- email (unique, indexed)
- password_hash
- name
- risk_tolerance (low/medium/high)
- horizon_years
- monthly_sip
- max_stock_allocation_pct (default 10)
- ui_mode (beginner/pro)
- created_at

### stocks
- id (uuid, pk)
- symbol (indexed)
- exchange (NSE/BSE/NYSE/NASDAQ, indexed)
- isin (nullable, indexed)
- cik (nullable)
- company_name (indexed)
- sector
- industry
- currency
- country
- market_cap
- last_updated

### price_history
- id (bigserial pk)
- stock_id (fk, indexed)
- date (indexed)
- open/high/low/close/volume
- adjusted_close
- UNIQUE(stock_id, date)

### financial_statements
- id (bigserial pk)
- stock_id (fk, indexed)
- period_type (annual/quarterly)
- fiscal_period
- revenue, cogs, ebit, net_income, eps
- cfo, cfi, cff, fcf
- total_assets, total_liabilities, equity, debt, cash
- shares_outstanding
- UNIQUE(stock_id, period_type, fiscal_period)

### valuation_snapshots
- id (bigserial pk)
- stock_id (fk, indexed)
- as_of_date (indexed)
- pe_ttm, pe_fwd, peg, ps, pb, ev_ebitda, ev_sales, ev_fcf
- roce, promoter_holding, promoter_pledge

### technical_snapshots
- id (bigserial pk)
- stock_id (fk, indexed)
- as_of_date
- sma20, sma50, sma100, sma200
- ema20, ema50, ema100, ema200
- rsi14, macd, macd_signal, bb_upper, bb_lower, atr14
- trend_label, support_zone, resistance_zone

### ownership_snapshots
- id (bigserial pk)
- stock_id (fk, indexed)
- as_of_date
- promoter_pct
- institutional_pct
- insider_pct
- float_shares

### events
- id (bigserial pk)
- stock_id (fk, indexed)
- event_type (earnings/dividend/split/bonus)
- event_date (indexed)
- payload_json

### news_items
- id (bigserial pk)
- stock_id (fk, indexed)
- published_at (indexed)
- source
- headline
- url
- sentiment_label
- sentiment_score

### portfolios
- id (uuid, pk)
- user_id (fk, indexed)
- name
- base_currency
- created_at

### holdings
- id (uuid, pk)
- portfolio_id (fk, indexed)
- stock_id (fk, indexed)
- quantity
- avg_price
- purchase_date
- UNIQUE(portfolio_id, stock_id)

### watchlists
- id (uuid, pk)
- user_id (fk, indexed)
- name

### watchlist_items
- watchlist_id (fk, indexed)
- stock_id (fk, indexed)
- added_at
- PRIMARY KEY(watchlist_id, stock_id)

### glossary_terms
- key (pk)
- name
- definition
- formula
- interpretation
- good_bad_ranges
- common_mistakes

## Indexes
- `idx_stocks_symbol_exchange` on stocks(symbol, exchange)
- `idx_price_history_stock_date` on price_history(stock_id, date desc)
- `idx_financials_stock_period` on financial_statements(stock_id, period_type, fiscal_period desc)
- `idx_events_stock_date` on events(stock_id, event_date desc)
- `idx_news_stock_published` on news_items(stock_id, published_at desc)
