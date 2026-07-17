from lse.client import LSE


client = LSE("lse_live_de2a62bd8d03a6a6376d54cecf828830")


def get_signal():

    data = client.candles(
        "EUR/USD",
        timeframe="1m",
        limit=50
    )

    closes = [c["close"] for c in data]

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
        "price": round(price,5),
        "ema21": round(ema21,5),
        "difference": round(diff,3)
    }
