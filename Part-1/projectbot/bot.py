from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler
from telegram.ext import MessageHandler, Filters
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


updater = Updater('5735181424:AAEcc1Wlx-XRk00-bIVfAun33MuzDE-FwSc')
dispatcher = updater.dispatcher

def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

echo_handler = MessageHandler(), echo
dispatcher.add_handler(echo_handler)

#def unknown(update: Update, context: CallbackContext):
#    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

#unknown_handler = MessageHandler(Filters.command, unknown)
#dispatcher.add_handler(unknown_handler)

def caps(update: Update, context: CallbackContext):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
updater.idle()