from telegram.ext import (
    Updater, CallbackContext, CommandHandler, MessageHandler, Filters, ConversationHandler)
from telegram import Update
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

STEP_ONE, STEP_TWO, STEP_THREE = range(3)

user_params = []

def recommendation(imt):
    if imt < 2:
        return 'у вас все ОК. Молодець'
    else:
        return 'Not OK'


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm a weight bot. Перевірити масу тіла /weight")


def question_1(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="enter your weight(in kilograms)")
    return STEP_TWO


def question_2(update, context):
    user_params.append(update.message.text) 
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Now enter your height(in centimeters")
    return STEP_THREE



def calculation(update, context):
    user_height = update.message.text 
    imt_calc = int(user_params[0]) / int(user_height)
    message = recommendation(imt_calc)

    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text=message)
    return ConversationHandler.END  



def cancel(update, context):
    update.message.reply_text('Cancelled by user. Send /menu to start again')
    return ConversationHandler.END


updater = Updater(token='5365655975:AAF7UvbaTKd1rDUnakCsvCP9lJsTYkwXrwA', use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))
branch_user_handler = ConversationHandler(
    entry_points = [CommandHandler('weight', question_1)], 
    states={

        STEP_TWO:   [MessageHandler(Filters.text & (~ Filters.command), question_2)],
        STEP_THREE: [MessageHandler(Filters.text & (~ Filters.command), calculation)]
    }, 
    fallbacks=[CommandHandler("stop", cancel)]
)

dispatcher.add_handler(branch_user_handler)
updater.start_polling()

