from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CallbackQueryHandler, CommandHandler, ConversationHandler, CallbackContext, MessageHandler, Filters

user_info = dict()


def start(update: Update, context: CallbackContext):
    menu(update, context)


def menu(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("привіт", callback_data="info")]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("інфо", reply_markup=reply_markup)


def user_business(update, context) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Як справи?")
    return 1


def user_business_2(update, context) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text='Як пройшов день?')
    return ConversationHandler.END

def user_name(update, context):
    chat = update.effective_chat
    user_info['name'] = update.message.text 
    user_text =  user_info.get('name') 

def back(update, context):
    update.message.reply_text('натисни  знову старт щоб перезапустити бота')
    return ConversationHandler

def help_command(update: Update, context: CallbackContext):
    pass

def main() -> None:
    updater = Updater(token='5365655975:AAF7UvbaTKd1rDUnakCsvCP9lJsTYkwXrwA')
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('menu', menu))
    # dispatcher.add_handler(CommandHandler("допомога", help_command))
    # dispatcher.add_handler(CommandHandler("повернутися", back))

    # stopfile=[CommandHandler("зупинка", back)]
    
    
    user_handler = ConversationHandler(
        entry_points = [CallbackQueryHandler(user_business, 'info')],
        states={
            # 1:  [MessageHandler(Filters.text & (~ Filters.command), user_business)],
            1:  [MessageHandler(Filters.text & (~ Filters.command), user_business_2)],
        },
        fallbacks=[CommandHandler("stop", back)]
    )    
    
    
    dispatcher.add_handler(user_handler) 
    updater.start_polling()
    updater.idle()
        
        
if __name__ == "__main__":
    main()