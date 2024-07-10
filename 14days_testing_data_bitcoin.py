import requests
from datetime import datetime, timedelta

def get_historical_data(coin_id, vs_currency, days):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {
        "vs_currency": vs_currency,
        "days": days,
        "interval": "daily"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def print_historical_data(coin_id, vs_currency):
    data = get_historical_data(coin_id, vs_currency, 14)
    if data:
        prices = data['prices']
        print(f"Historical data for {coin_id} in {vs_currency.upper()}:")
        for price in prices:
            date = datetime.fromtimestamp(price[0] / 1000).strftime('%Y-%m-%d')
            print(f"Date: {date}, Price: {price[1]:.2f} {vs_currency.upper()}")
    else:
        print(f"Failed to retrieve data for {coin_id} in {vs_currency.upper()}")

coins = ["bitcoin", "ethereum", "litecoin"]
currencies = ["usd", "thb", "jpy"]

for coin in coins:
    for currency in currencies:
        print_historical_data(coin, currency)
        print()
