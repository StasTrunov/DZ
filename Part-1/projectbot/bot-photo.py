from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters

import os

img_directory = 'D:\goit\lections\project-bot\photo'


def start(update: Update, context: CallbackContext):
    message = '''Я демо-бот для роботи з фото. Основні команди [та їх параметри]:
        /list - перегляд списку всіх фото
        /show [файл] - показати конкретне фото'''
    context.bot.send_message(chat_id = update.effective_chat.id, text = message) 


def photo_list(update: Update, context: CallbackContext):
    message = 'список фото:\n'
    photoes = list()
    files = os.listdir(img_directory)
    for f in files:
        if '.jpg' in f:
            #only image format jpg 
            photoes.append(f)

    message += '\n'.join(photoes)
    context.bot.send_message(chat_id = update.effective_chat.id, text = message) 


def photo_add(update: Update, context: CallbackContext):
    try:
        file = context.bot.getFile(update.message.photo[0].file_id)
        photo_name = update.message.caption + '.jpg'
        file_name = os.path.join(img_directory, photo_name)
        file.download(custom_path=file_name)
        context.bot.send_message(chat_id = update.effective_chat.id, text = "Фото завантажено успішно. Список фото /list")
    except:
        context.bot.send_message(chat_id = update.effective_chat.id, text = "Помилка при завантажені. Список фото /list") 

# /show 7A.jpg
def photo_show(update: Update, context: CallbackContext):
    photo_name = context.args
    file = os.path.join(img_directory, photo_name[0])
    
    if os.path.exists(file):
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(file, 'rb'))
    else:
        context.bot.send_message(chat_id = update.effective_chat.id, text = 'Файл не знайдено') 


def unknown(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Невідома команда. Бот не знає що робити :(((  Спробуй '/start' ")


updater = Updater(token='5604588240:AAEAEyS-jZpziKuYZygvf4JKa2-MwUgxzEA')
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('list', photo_list))
dispatcher.add_handler(CommandHandler('show', photo_show))

dispatcher.add_handler(MessageHandler(Filters.photo, photo_add))


unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
updater.idle()