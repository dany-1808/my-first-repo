import requests

API_KEY = "CHJNQ2ED420YFYKD"

BASE = "EUR"
QUOTE = "USD"

url = (
    f"https://www.alphavantage.co/query"
    f"?function=FX_INTRADAY"
    f"&from_symbol={BASE}"
    f"&to_symbol={QUOTE}"
    f"&interval=1min"
    f"&outputsize=compact"
    f"&apikey={API_KEY}"
)

data = requests.get(url, timeout=20).json()

print(data)
