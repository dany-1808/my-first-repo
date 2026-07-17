from message import make_message


signal = {
    "pair": "EUR/USD",
    "signal": "BUY",
    "quality": "B",
    "price": 1.46909,
    "ema21": 1.46847,
    "difference": 0.042,
    "stop": 1.46762,
    "target": 1.47203
}


print(make_message(signal))
