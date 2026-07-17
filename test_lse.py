from lse.client import LSE

client = LSE("lse_live_de2a62bd8d03a6a6376d54cecf828830")

data = client.candles(
    "EUR/USD",
    timeframe="1m",
    limit=10
)

for candle in data:
 print(
    candle["timestamp"],
    "\n Open:", candle["open"],
    "\n High:", candle["high"],
    "\n Low:", candle["low"],
    "\n Close:", candle["close"],
    "\n---"
)
