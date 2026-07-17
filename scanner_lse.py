from lse.client import LSE
from datetime import datetime
import time


client = LSE("lse_live_de2a62bd8d03a6a6376d54cecf828830")


last_signal = None


def analyze():

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


    stop = None
    target = None


    if signal == "BUY":

        stop = price * 0.999
        target = price * 1.002


    elif signal == "SELL":

        stop = price * 1.001
        target = price * 0.998



    result = {

        "time": str(datetime.now()),

        "pair": "EUR/USD",

        "signal": signal,

        "quality": quality,

        "price": round(price,5),

        "ema21": round(ema21,5),

        "difference": round(diff,3),

        "stop": round(stop,5) if stop else None,

        "target": round(target,5) if target else None

    }


    return result



while True:


    result = analyze()


    print("----------------------------")
    print(result)


    if result["signal"] != "WAIT" and result["signal"] != last_signal:


        with open("signals.txt","a") as file:

            file.write(str(result))
            file.write("\n----------------------------\n")


        print("✅ Новый сигнал сохранён")


        last_signal = result["signal"]


    else:

        print("Ждём...")


    time.sleep(60)
