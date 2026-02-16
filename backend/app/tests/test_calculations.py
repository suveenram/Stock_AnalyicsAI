from app.services.calculations import (
    allocation_percent_by_risk,
    cagr,
    confidence_band,
    valuation_percentile,
)


def test_cagr():
    result = cagr(100, 121, 2)
    assert round(result, 4) == 0.1


def test_cagr_invalid():
    assert cagr(-1, 100, 3) is None


def test_valuation_percentile():
    assert valuation_percentile(20, [10, 20, 30, 40]) == 50.0


def test_allocation_percent():
    assert allocation_percent_by_risk("low", "high") <= 5


def test_confidence_band():
    assert confidence_band(60) == "52-68%"
