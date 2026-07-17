from lse.client import LSE
from datetime import datetime


client = LSE("lse_live_de2a62bd8d03a6a6376d54cecf828830")


data = client.candles(
    "EUR/USD",
    timeframe="1m",
    limit=50
)


closes = [c["close"] for c in data]

first = closes[0]
last = closes[-1]


# EMA21
ema = sum(closes[-21:]) / 21

diff = ((last - ema) / ema) * 100


# последние 3 свечи
last_three = closes[-3:]

above = all(price > ema for price in last_three)
below = all(price < ema for price in last_three)


signal = "⚪ WAIT"
trend = "➡️ нет уверенности"
quality = "C"


if above and diff > 0.03:

    signal = "🟢 BUY"
    trend = "📈 вверх"

    if diff > 0.05:
        quality = "A"
    else:
        quality = "B"


elif below and diff < -0.03:

    signal = "🔴 SELL"
    trend = "📉 вниз"

    if diff < -0.05:
        quality = "A"
    else:
        quality = "B"


print("EUR/USD анализ")
print("----------------------------")
print("Первая цена:", first)
print("Последняя цена:", last)
print("EMA21:", ema)
print("Отклонение:", round(diff, 3), "%")
print("----------------------------")
print("Тренд:", trend)
print("Сигнал:", signal)
print("Качество:", quality)


if signal != "⚪ WAIT":

    if signal == "🟢 BUY":
        stop = last * 0.999
        target = last * 1.002

    else:
        stop = last * 1.001
        target = last * 0.998


    print("----------------------------")
    print("Вход:", last)
    print("Стоп:", round(stop, 5))
    print("Цель:", round(target, 5))


    with open("signals.txt", "a") as file:
        file.write(f"""
Время: {datetime.now()}
Пара: EUR/USD
Сигнал: {signal}
Качество: {quality}
Вход: {last}
Стоп: {round(stop,5)}
Цель: {round(target,5)}
EMA21: {ema}
Отклонение: {round(diff,3)}%
----------------------------
""")


    print("✅ Сигнал сохранён")

else:

    print("Сделка не открыта")
