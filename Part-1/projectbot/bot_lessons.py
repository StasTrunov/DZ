# pip install python-telegram-bot

# https://core.telegram.org/bots/api

# https://github.com/python-telegram-bot/v13.x-wiki/wiki/Extensions-–-Your-first-Bot

# https://github.com/python-telegram-bot/v13.x-wiki/wiki/Types-of-Handlers

# https://docs.python-telegram-bot.org/en/v13.13/telegram.bot.html
# https://docs.python-telegram-bot.org/en/v13.13/telegram.ext.updater.html
# https://docs.python-telegram-bot.org/en/v13.13/telegram.ext.dispatcher.html

# https://docs.python-telegram-bot.org/en/v13.13/telegram.update.html
# https://docs.python-telegram-bot.org/en/v13.13/telegram.ext.callbackcontext.html


# https://docs.python-telegram-bot.org/en/v13.13/telegram.ext.messagehandler.html
# https://docs.python-telegram-bot.org/en/stable/telegram.ext.filters.html


from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler,  MessageHandler, Filters
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


def caps(update: Update, context: CallbackContext):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


updater = Updater('5600103048:AAEqpzoHClYthjRlzQ_NoGP7kBGOhVlyG_w')
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('caps', caps))

dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))


updater.start_polling()
updater.idle()






















# from telegram import Update
# from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
# import logging


# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# def start(update: Update, context: CallbackContext):
#     context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

# def echo(update: Update, context: CallbackContext):
#     context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# def caps(update: Update, context: CallbackContext):
#     text_caps = ' '.join(context.args).upper()
#     context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

# def unknown(update: Update, context: CallbackContext):
#     context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

# updater = Updater(token='5654146188:AAGPmhjntIMT64lc9Wq5MjQCNL458q8QoYw')
# dispatcher = updater.dispatcher

# start_handler = CommandHandler('start', start)
# dispatcher.add_handler(start_handler)

# echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
# dispatcher.add_handler(echo_handler)

# caps_handler = CommandHandler('caps', caps)
# dispatcher.add_handler(caps_handler)

# unknown_handler = MessageHandler(Filters.command, unknown)
# dispatcher.add_handler(unknown_handler)

# updater.start_polling()
# updater.idle()