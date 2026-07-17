import requests


def get_price():
    try:
        url = "https://open.er-api.com/v6/latest/USD"
        data = requests.get(url, timeout=10).json()

        return float(data["rates"]["EUR"])

    except Exception as e:
        print("Ошибка цены:", e)
        return None


def get_signal():

    price = get_price()

    if price is None:
        return {
            "pair": "EUR/USD",
            "signal": "WAIT",
            "quality": "C",
            "price": 0,
            "ema21": 0,
            "difference": 0
        }


    ema21 = price

    diff = 0


    signal = "WAIT"
    quality = "C"


    return {
        "pair": "EUR/USD",
        "signal": signal,
        "quality": quality,
        "price": round(price,5),
        "ema21": round(ema21,5),
        "difference": round(diff,3)
    }
