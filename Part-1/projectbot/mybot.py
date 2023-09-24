from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler # MessageHandler, Filters
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="What's your name")
    name = update.message.text
    if name:
        context.bot.send_message(chat_id = update.effective_chat.id, text = 'How old are you')
    old = update.message.text
    if old < 4:
        context.bot.send_message(chat_id = update.effective_chat.id, text = 'You are small baby')
    if old < 7:
        context.bot.send_message(chat_id = update.effective_chat.id, text = 'You are baby')
    elif old < 10:
        context.bot.send_message(chat_id = update.effective_chat.id, text = 'You are child')
    elif old < 18:
        context.bot.send_message(chat_id = update.effective_chat.id, text = 'You are teenager')
    elif old > 18:
        context.bot.send_message(chat_id = update.effective_chat.id, text = 'You are adult')
    elif old > 50:
        context.bot.send_message(chat_id = update.effective_chat.id, text = 'You are old')
    elif old > 80:
        context.bot.send_message(chat_id = update.effective_chat.id, text = 'You are very old')
    elif old > 150:
        context.bot.send_message(chat_id = update.effective_chat.id, text = 'You are the oldest')

    context.bot.send_message(chat_id = update.effective_chat.id, text = 'Where are you from')


def main() -> None:
    updater = Updater(token='5582099194:AAEmYEOCk9J6ynEpuFwqFF2t5QclxiJkHkM')
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(start)

    updater.start_polling()
    updater.idle()
    #print('start bot')


if __name__ == "__main__":
    main()