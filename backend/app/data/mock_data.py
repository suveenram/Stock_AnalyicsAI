STOCKS = {
    "AAPL": {
        "symbol": "AAPL",
        "exchange": "NASDAQ",
        "company_name": "Apple Inc.",
        "sector": "Technology",
        "industry": "Consumer Electronics",
        "quote": {"price": 215.3, "change_pct": 0.82},
        "key_metrics": {"pe_ttm": 28.1, "pb": 43.2, "roe": 152.4, "debt_equity": 1.45},
        "technical": {
            "trend": "bullish",
            "risk_grade": "medium",
            "support": 205.0,
            "resistance": 222.0,
            "indicators": {"rsi": 62.1, "sma20": 210.2, "sma50": 201.5, "atr": 3.8},
            "signals": ["Price above SMA20 and SMA50", "Volume breakout confirmation in last 5 sessions"],
        },
    },
    "RELIANCE.NS": {
        "symbol": "RELIANCE.NS",
        "exchange": "NSE",
        "company_name": "Reliance Industries Ltd",
        "sector": "Energy",
        "industry": "Integrated Oil & Gas",
        "quote": {"price": 2998.0, "change_pct": -0.26},
        "key_metrics": {"pe_ttm": 25.2, "pb": 2.1, "roe": 8.8, "debt_equity": 0.42, "promoter_holding": 50.3},
        "technical": {
            "trend": "neutral",
            "risk_grade": "medium",
            "support": 2870.0,
            "resistance": 3060.0,
            "indicators": {"rsi": 51.3, "sma20": 2978.2, "sma50": 2944.1, "atr": 45.5},
            "signals": ["Range-bound price action", "Await breakout above resistance for trend confirmation"],
        },
    },
}

GLOSSARY = {
    "pe_ttm": {
        "name": "P/E (TTM)",
        "definition": "Price divided by trailing 12-month earnings per share.",
        "formula": "Market Price per Share / EPS (TTM)",
        "interpretation": "Higher may imply growth expectations; lower may imply value or risk.",
        "good_bad_ranges": "Contextual by sector; compare against peers and 5Y band.",
        "common_mistakes": "Using P/E when EPS is negative.",
    }
}
