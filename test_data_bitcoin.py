import requests
import pyfiglet

def get_bitcoin_data():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd,thb,jpy"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_robot_icon():
    ascii_art = pyfiglet.figlet_format("Mr. Richy")
    print(ascii_art)
display_robot_icon()
bitcoin_data = get_bitcoin_data()
if bitcoin_data:
    usd_price = bitcoin_data['bitcoin']['usd']
    thb_price = bitcoin_data['bitcoin']['thb']
    jpy_price = bitcoin_data['bitcoin']['jpy']
    print(f"Current Bitcoin price in USD: ${usd_price}")
    print(f"Current Bitcoin price in THB: ฿{thb_price}")
    print(f"Current Bitcoin price in JPY: ¥{jpy_price}")
else:
    print("Failed to retrieve data")

