from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackContext, CommandHandler,  MessageHandler, Filters,CallbackQueryHandler, ConversationHandler
import logging
from random import choices
import time

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def scrambl(update: Update, context: CallbackContext):
    scrambl = ["R", "R'", "R2", "L", "L'", "L2", "F", "F'", "F2", "D", "D'", "D2", "B", "B'", "B2"]
    x = 0
    list_ = []
    while True:
        for i in choices(scrambl):
            list_.append(i)
            x +=1
        if x == 14:
            break
    
    context.bot.send_message(chat_id=update.effective_chat.id, text=list_)


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello")


def stop_stopwatch(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Stop", callback_data="Stop"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Если вы закончили сборку нажмите кнопку Stop", reply_markup=reply_markup
    )

def start_stopwatch(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton("Start", callback_data="Start"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Если хотите начать сборку, нажмите кнопку Start", reply_markup=reply_markup)

def stopwatch(update:Update, context:CallbackContext):
    sec = 0
    query = update.callback_query
    query.answer()
    while True:
        if query.data == 'Start':
            time.sleep(1)
            sec += 1
            context.bot.send_message(chat_id=update.effective_chat.id, text=sec)

def button(update:Update, context:CallbackContext):
    query = update.callback_query
    query.answer()
    if query.data == 'Start':
        stop_stopwatch(update, context)
    elif query.data == 'Stop':
        return ConversationHandler.END
    
user_handler = ConversationHandler(
        entry_points = [CommandHandler('start_stopwatch', start_stopwatch)],
        states={
        1:  [(CallbackQueryHandler(button))],
        2:  [(CallbackQueryHandler(stop_stopwatch))]
          },
        fallbacks=[(CallbackQueryHandler(stop_stopwatch))])




updater = Updater('5582099194:AAEmYEOCk9J6ynEpuFwqFF2t5QclxiJkHkM')
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('scrambl', scrambl))
#dispatcher.add_handler(CommandHandler('start_stopwatch', start_stopwatch))
# button_handler = (CallbackQueryHandler(button))
# dispatcher.add_handler(button_handler)
button_handler = (CallbackQueryHandler(button))
dispatcher.add_handler(button_handler)
updater.start_polling()
updater.idle()