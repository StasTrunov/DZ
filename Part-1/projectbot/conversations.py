# https://docs.python-telegram-bot.org/en/v13.13/telegram.ext.conversationhandler.html

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CallbackQueryHandler,
    CommandHandler,
    ConversationHandler,
    CallbackContext, 
    MessageHandler, 
    Filters
)

user_data = dict()

#Stages
STEP_ONE, STEP_TWO, STEP_THREE, STEP_FOUR = range(4)


def start(update: Update, context: CallbackContext) -> None:
    menu(update, context)


def menu(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Користувач", callback_data="user_info"),
            InlineKeyboardButton("Організація", callback_data="company_info"),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Введіть необхідну інформацію", reply_markup=reply_markup)
    


def company_info(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Інформація про компанію отримана автоматично. Дякуємо.")

    

def user_name(update, context) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="enter your name")
    return STEP_TWO


def user_email(update, context):
    chat = update.effective_chat
    user_data['name'] = update.message.text 

    context.bot.send_message(chat_id=chat.id, text="enter your email ")
    return STEP_THREE    


def user_phone(update, context):
    chat = update.effective_chat
    user_data['mail'] = update.message.text 

    context.bot.send_message(chat_id=chat.id, text="enter your phone ")
    return STEP_FOUR    


def user_finish(update, context):
    chat = update.effective_chat
    user_data['phone'] = update.message.text

    user_text = "Thanks " + user_data.get('name') + " 😉"

    context.bot.send_message(chat_id=chat.id, text=user_text)
    return ConversationHandler.END  


def cancel(update, context):
    update.message.reply_text('Cancelled by user. Send /menu to start again')
    return ConversationHandler.END


def main() -> None:
    updater = Updater(token='5654146188:AAGPmhjntIMT64lc9Wq5MjQCNL458q8QoYw')
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("menu", menu))
    dispatcher.add_handler(CallbackQueryHandler(company_info, pattern="company_info"))

    branch_user_handler = ConversationHandler(
        entry_points = [CallbackQueryHandler(user_name, 'user_info')], 
        states={
            STEP_TWO:   [MessageHandler(Filters.text & (~ Filters.command), user_email)],
            STEP_THREE: [MessageHandler(Filters.text & (~ Filters.command), user_phone)],
            STEP_FOUR:  [MessageHandler(Filters.text & (~ Filters.command), user_finish)]
        }, 
        fallbacks=[CommandHandler("stop", cancel)]
    )

    dispatcher.add_handler(branch_user_handler)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()