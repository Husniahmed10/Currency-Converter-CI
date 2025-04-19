import pytest
from src.converter import convert_currency

def test_convert_currency(monkeypatch):
    def mock_get_exchange_rate(base, target):
        return 0.85 

    from src.converter import get_exchange_rate
    monkeypatch.setattr("src.converter.get_exchange_rate", mock_get_exchange_rate)

    assert convert_currency(100, "EUR", "USD") == 85.00
