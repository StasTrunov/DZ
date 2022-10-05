#programma GORODA

#from tracemalloc import stop
from encodings import utf_8
from ast import Global
from tkinter import W
from turtle import circle
from telegram import Update
from telegram.ext import Updater,CallbackContext, CommandHandler, MessageHandler, Filters,ConversationHandler
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def format_array_ukr_cities():  #Форматує міста зі списка. Список українських міст отриманий читанням з файла
    i=0 
    while i<len(array_ukr_cities):
        if i==0:
            array_ukr_cities[i]=array_ukr_cities[i][1:-1]
        else:
            array_ukr_cities[i]=array_ukr_cities[i][:-1]
        array_ukr_cities[i]=array_ukr_cities[i].lower()
        i+=1

def init_alphabet_ukr(): #Підраховує та записує в -alphabet_ukr- скільки є українських міст, які починаються на задану букву
    for x in alphabet_ukr:
        for y in array_ukr_cities:
            if x[0]==y[0]:
                x[1]+=1

def find_next_chair(city):  #Шукає в введеному місті останню букву з якої повинно починатись наступне місто
     array_ukr_cities.remove(city)
     cities_named.append(city)
     n=-1
     i=0
     while i<len(alphabet_ukr):
          if n==-len(city):
               return ''
          elif alphabet_ukr[i][0]==city[n] and alphabet_ukr[i][1]!=0:
               alphabet_ukr[i][1]-=1
               return city[n]
          elif alphabet_ukr[i][0]==city[n] and alphabet_ukr[i][1]==0:
               n-=1
               i=0
          else:
               i+=1

def computer_algorithm_generate_city (chair):  #Алгорітм вибору комп'ютером міста. Він бере перше місто у списку. Міста початково відсортировані у порядку чисельності населення
    for i in array_ukr_cities:
        if i[0]==chair:
            return i

def city_play(update, context):
    #global circle_game_max
    global circle_game
    global chair
    global attempt
    global help_gamer

    attempt+=1
    city_input=update.message.text
    city=city_input.lower()
    match attempt:
       case 0:
        end_string=', спробуй ще раз (залишилось 3 спроби)'
       case 1:
        end_string=', спробуй ще раз (залишилось 2 спроби)'
       case 2:
        end_string=', спробуй ще раз (залишилась 1 спроба)'
       case 3:
        end_string='.' 
    if city=='стоп':   
        update.message.reply_text('Ти ввів СТОП, що означає закінчення гри')
        return 2
    elif city in cities_named:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Таке місто вже називали'+end_string)
    elif city not in array_ukr_cities:
        update.message.reply_text('Такого міста в Україні не існує'+end_string)      
    elif chair!=city[0] and chair != ' ':
        txt = 'Треба ввести місто назва якого починається з букви - '+chair.capitalize()+' -,а не з букви - '+city[0].capitalize()+' - '+end_string
        update.message.reply_text(txt)
    else:
        attempt=0
        circle_game+=1
        chair=find_next_chair(city)
        if chair=='':
            update.message.reply_text('У мене не залишилось варіантів назвати місто. ТИ ВИГРАВ!!!!!')
            update.message.reply_text('Твій результат: -'+str(circle_game-help_gamer+100)+'-\nТИ ДУЖЕ КРУТИЙ - ВІТАЮ!!!!!')
            return 2
        update.message.reply_text('Мені потрібно назвати місто на букву -'+chair.capitalize()+'-')
        city=computer_algorithm_generate_city(chair)
        update.message.reply_text('Я називаю місто: '+city.capitalize())
        chair=find_next_chair(city)
        if chair=='':
            update.message.reply_text('У тебе не залишилось варіантів назвати місто. Я виграв')
            update.message.reply_text('Твій результат: -'+str(circle_game-help_gamer)+'-\nНе засмучуйся, наступного разу буде краще')
            return 2
        update.message.reply_text('КОЛО -'+str(circle_game)+' -') 
        update.message.reply_text('Тобі потрібно назвати місто на букву: -'+chair.capitalize()+'-')
    if attempt==3:
        update.message.reply_text('На жаль ти зробив 3 невірні спроби поспіль, що озачає програш')
        update.message.reply_text('Твій результат: -'+str(circle_game-help_gamer)+'-\nНе засмучуйся, наступного разу буде краще...')
        return 2

alphabet_ukr=[['а',0],['б',0],['в',0],['г',0],['д',0],['е',0],['є',0],['ж',0],['з',0],['и',0],['і',0],['ї',0],
              ['й',0],['к',0],['л',0],['м',0],['н',0],['о',0],['п',0],['р',0],['с',0],['т',0],['у',0],['ф',0],
              ['х',0],['ц',0],['ч',0],['ш',0],['щ',0],['ь',0],['ю',0],['я',0],[' ',0],["'",0],['-',0]]

fh = open(r'C:\Users\PC\Desktop\Python\mybots\All_cities.txt', encoding="UTF-8")
array_ukr_cities = fh.readlines()
fh.close()
format_array_ukr_cities ()
init_alphabet_ukr ()
cities_named = list ()
chair=' '
attempt=0
circle_game=1
help_gamer=0

def start(update, context):
    update.message.reply_text('Давай пограємо в дуже цікаву гру - МІСТА УКРАЇНИ -\n')
    txt = "Для старту гри потрібно зареєструвати Ігрока\n"
    update.message.reply_text(txt)
    #context.bot.send_message(chat_id=update.effective_chat.id, text='тільки є одна умова - всі міста повинні бути в Україні.\nНу почнемо! Введи будь-яке українське місто:\nКОЛО -1-')
    update.message.reply_text("Введи свое Прізвище та Ім'я (бажано на українській мові) і пін-код\nЗразок: Шевченко Тарас 1234")#+'\n'
    #user(update, context)
    return 1
    

def stop (update, context):  
    update.message.reply_text('Ти ввів СТОП, що озачає закінчення гри')
    update.message.reply_text('Твій результат: -'+str(circle_game-help_gamer)+'-\nНе засмучуйся, наступного разу буде краще...')
    return ConversationHandler.END

def rules (update, context):
    txt1 = '                   Правила Гри -МІСТА УКРАЇНИ- (ШІ-Штучний інтелект)\n'
    txt2 = '     1. Міста повинні бути тільки українськими та вводяться українською мовою.\n'
    txt3 = '     2. Введення назв сел, селищ та селищ міського типу не допускається.\n'
    txt4 = "     3. Спочатку Ігрок реєструється командою /user (бажано ввести своє Ім'я та Прізвище)\n"
    txt5 = '     4. У Ігрока є три спроби назвати місто. Якщо всі спроби хибні, то він програє.\n'
    txt6 = "     5. У Ігрока є три підказки від ШІ. Щоб цим скористатися треба ввести /help\n"
    txt7 = '     6. Наступне місто треба назвати на останню букву міста яке тільки що називалося.\n'
    txt8 = "     7. Якщо таких міст не існує, ШІ автоматично бере передостанню букву, і так далі.\n"
    txt9 = '     8. Гра закінчується, якщо неможливо назвати наступне місто перебираючи всі букви названого міста.\n'
    txt10 = '     9. Ігрок може закінчити ігру примусово, ввівши команду /stop .Для нової гри треба ввести /start\n'
    txt11 = '     10. Результат Ігрока це: Номер КОЛА - Число Підказок + 100 балів за виграш у ШІ.\n'
    txt12 = '     11. Всі результати зберігаються. Кращі 20 результатів можно вивести командою /scores.\n'
    txt13 = '                       - БАЖАЄМО ПЕРЕМОГИ, СЛАВА УКРАЇНІ!!! -\n'
    update.message.reply_text(txt1+txt2+txt3+txt4+txt5+txt6+txt7+txt8+txt9+txt10+txt11+txt12+txt13)


def check_name(last_first_name):
    name_without_space=last_first_name.replace(' ','')
    if last_first_name.count(' ')!=1:
        return False
    elif not name_without_space.isalpha():
        return False
    else:
        return True

def check_pin(pin):
    return pin.isdecimal()

def user (update, context):
     fh = open(r'C:\Users\PC\Desktop\Python\mybots\Scores.txt','r+',encoding='UTF-8')
     gamer_scores = fh.readlines()
     user_input = update.message.text
     name=user_input[:-6]
     pin=user_input[-5:-1]


     if not check_name(name) and not check_pin(pin):
          update.message.reply_text("Введіть правильно Прізвище та І'мя, а також пін-код")
     elif not check_name(name):
          update.message.reply_text("Введіть правильно Прізвище та І'мя")
     elif not check_pin(pin):
          update.message.reply_text('Введіть правильно пін-код')
     elif name.title()+'\n' in gamer_scores and gamer_scores[gamer_scores.index(name.title()+'\n')+1]!=pin+'\n':
          update.message.reply_text("Ігрок з таким Прізвищем та І'мям вже існує, введіть іншу назву...\nабо якщо це саме Ви, введіть вірний пін-код")
     else:
          if name.title()+'\n' in gamer_scores and gamer_scores[gamer_scores.index(name.title()+'\n')+1]==pin+'\n':
               update.message.reply_text('Ласкаво просимо до гри '+name.title()+'. Ваш кращий результат: '+gamer_scores[gamer_scores.index(name.title()+'\n')+2])
               update.message.reply_text('Почнемо гру...\n')
          else:
               print(name.title(),file=fh)
               print(pin,file=fh)
               print('0',file=fh)
               update.message.reply_text('Ласкаво просимо до гри '+name.title()+'. Ви граєте перший раз, тому нагадуємо\n прочитати правила ги - /rules подивитесь топ-20 результатів - /scores\nпідказка від ШІ - /help остановити гру - /stop')
               update.message.reply_text('Почнемо гру...\n')
     fh.close()

def scores (update, context):
     fh = open(r'C:\Users\PC\Desktop\Python\mybots\Scores.txt','r+',encoding='UTF-8')
     gamer_scores_read = fh.readlines()
     fh.close()
     del gamer_scores_read[1::3]
     gamer_scores_for_print=[[0 for i in range (2)] for y in range(int(len(gamer_scores_read)/2))]
     for i in range(int(len(gamer_scores_read)/2)):
          gamer_scores_for_print[i][1]=(gamer_scores_read[i*2].replace('\n',''))
          gamer_scores_for_print[i][0]=int(gamer_scores_read[i*2+1].replace('\n',''))

     gamer_scores_for_print=sorted(gamer_scores_for_print, reverse=True)
     update.message.reply_text(gamer_scores_for_print)


def help (update, context): 
    global help_gamer
    end_string='' 
    if help_gamer==3:
        update.message.reply_text('На жаль ти вичерпав всі три підказки')
    elif circle_game==1:
        update.message.reply_text('Ще занадто рано для підказки')
    else:
        help_gamer+=1
        city_help=computer_algorithm_generate_city(chair)
        match help_gamer:
            case 1:
                end_string = '(залишилося 2 підказки)'
            case 2:
                end_string = '(залишилася 1 підказка)'
            case 3:
                end_string = '(підказок більше немає)'  
        update.message.reply_text('Підказка: спробуй ввести місто -'+city_help.capitalize()+'-\n'+end_string)


def main() -> None:
    updater = Updater(token='5651601814:AAFGjtbWbKOLm0uGkjtH2lq4g4_Ke1FE4l4')
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CommandHandler('rules', rules))
    dispatcher.add_handler(CommandHandler('stop', stop))
    dispatcher.add_handler(CommandHandler('scores', scores))


    user_handler = ConversationHandler(
        entry_points = [CommandHandler('start', start)],
        states={
            1:  [MessageHandler(Filters.text & (~ Filters.command), user)],
            2:  [MessageHandler(Filters.text & (~ Filters.command), city_play)],
            3:  [CommandHandler("stop", stop)],
          },
          fallbacks=[CommandHandler('stop', stop)]
    )    

    dispatcher.add_handler(user_handler) 
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()