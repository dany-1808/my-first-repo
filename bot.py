from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from strategy_lse import get_signal


TOKEN = "8826058246:AAEFwCclOYoH9wLFgerv6R58ZqhaFd9zlQo"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🏹 Стрела AI запущена!\n\n"
        "/signal — анализ EUR/USD"
    )


async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🏹 Анализирую рынок..."
    )


    data = get_signal()


    if data["signal"] == "BUY":

        emoji = "🟢 BUY"

    elif data["signal"] == "SELL":

        emoji = "🔴 SELL"

    else:

        emoji = "⚪ WAIT"



    text = f"""
🏹 СТРЕЛА AI

💱 Пара: {data['pair']}

Сигнал: {emoji}

Качество: {data['quality']}

💰 Цена: {data['price']}

EMA21: {data['ema21']}

Отклонение: {data['difference']}%

"""


    await update.message.reply_text(text)



def main():

    app = Application.builder().token(TOKEN).build()


    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CommandHandler("signal", signal)
    )


    print("🏹 Стрела AI запущена")

    app.run_polling()



if __name__ == "__main__":

    main()
