import os
import requests


API_KEY = "8fd0c1a24918461e9639486ca3fe57df"


def get_signal():

    url = "https://api.twelvedata.com/time_series"

    params = {
        "symbol": "EUR/USD",
        "interval": "1min",
        "outputsize": 50,
        "apikey": API_KEY
    }

    try:
        r = requests.get(url, params=params, timeout=20)
        data = r.json()

        if "values" not in data:
            return {
                "pair": "EUR/USD",
                "signal": "ERROR",
                "quality": "C",
                "price": 0,
                "ema21": 0,
                "difference": 0
            }

        candles = data["values"]

        closes = [
            float(c["close"])
            for c in candles
        ]

        closes.reverse()

        price = closes[-1]

        ema21 = sum(closes[-21:]) / 21

        diff = ((price - ema21) / ema21) * 100


        last_three = closes[-3:]

        above = all(x > ema21 for x in last_three)
        below = all(x < ema21 for x in last_three)


        signal = "WAIT"
        quality = "C"


        if above and diff > 0.03:
            signal = "BUY"

            if diff > 0.05:
                quality = "A"
            else:
                quality = "B"


        elif below and diff < -0.03:
            signal = "SELL"

            if diff < -0.05:
                quality = "A"
            else:
                quality = "B"


        return {
            "pair": "EUR/USD",
            "signal": signal,
            "quality": quality,
            "price": round(price, 5),
            "ema21": round(ema21, 5),
            "difference": round(diff, 3)
        }


    except Exception as e:

        return {
            "pair": "EUR/USD",
            "signal": "ERROR",
            "quality": "C",
            "price": 0,
            "ema21": 0,
            "difference": 0,
            "error": str(e)
        }
