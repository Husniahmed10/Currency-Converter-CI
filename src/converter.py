import requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate.host/latest?base={base_currency}&symbols={target_currency}"
    response = requests.get(url)
    data = response.json()
    
    if "rates" in data and target_currency in data["rates"]:
        return data["rates"][target_currency]
    else:
        raise ValueError("Invalid currency code or API error.")

def convert_currency(amount, base_currency, target_currency):
    rate = get_exchange_rate(base_currency.upper(), target_currency.upper())
    return round(amount * rate, 2)
