def make_message(signal):

    if signal["signal"] == "BUY":
        emoji = "🟢 BUY"

    elif signal["signal"] == "SELL":
        emoji = "🔴 SELL"

    else:
        emoji = "⚪ WAIT"


    text = f"""
🚨 {signal['pair']}

{emoji}

Качество: {signal['quality']}

💰 Цена: {signal['price']}

🛑 Stop: {signal['stop']}
🎯 Target: {signal['target']}

EMA21: {signal['ema21']}
Отклонение: {signal['difference']}%
"""


    return text
