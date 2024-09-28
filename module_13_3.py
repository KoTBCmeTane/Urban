import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

logging.basicConfig(level=logging.INFO)

TOKEN = 'Токен'

async def start(update: Update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Привет! Я бот помогающий твоему здоровью.')

async def all_massages(update: Update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Введите команду /start, чтобы начать общение.')

def main():
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, all_massages))

    application.run_polling()

if __name__ == '__main__':
    main()