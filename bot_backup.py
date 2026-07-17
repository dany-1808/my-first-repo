import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8826058246:AAEFwCclOYoH9wLFgerv6R58ZqhaFd9zlQo"

PAIRS = [
    "EURUSD",
    "GBPUSD",
    "USDJPY",
    "USDCHF",
    "AUDUSD",
    "USDCAD",
    "NZDUSD"
]


def get_price(pair):
    try:
        base = pair[:3]
        quote = pair[3:]

        url = f"https://open.er-api.com/v6/latest/{base}"
        data = requests.get(url, timeout=10).json()

        return float(data["rates"][quote])

    except Exception as e:
        print("Ошибка данных:", e)
        return None


def analyze(pair):
    price = get_price(pair)

    if price is None:
        return f"⚪ {pair}: нет данных"

    # простая логика сигнала
    if price % 2 > 1:
        return f"🟢 {pair}: CALL\nЦена: {price}"

    elif price % 2 < 1:
        return f"🔴 {pair}: PUT\nЦена: {price}"

    return f"⏳ {pair}: ожидание"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏹 Стрела запущена!\n\n"
        "/pair — валютные пары\n"
        "/signal — сигналы"
    )


async def pair(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💱 Пары Стрелы:\n\n" + "\n".join(PAIRS)
    )


async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏹 Анализирую...")

    result = []

    for p in PAIRS:
        result.append(analyze(p))

    await update.message.reply_text(
        "\n\n".join(result)
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("pair", pair))
    app.add_handler(CommandHandler("signal", signal))

    print("🏹 Стрела запущена")

    app.run_polling()


if __name__ == "__main__":
    main()
