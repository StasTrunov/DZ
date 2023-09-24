#programma GORODA

from ast import Global
from tkinter import W
from turtle import circle
from unicodedata import name
from unittest import result
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
    if chair=='початок':
        for z in range(len(alphabet_ukr)):
            if city[0]==alphabet_ukr[z][0]:
                alphabet_ukr[z][1]-=1
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

def check_name(last_first_name):    #Перевірка Прізвища та Ім'я ігрока на коректність вводу
    name_without_space=last_first_name.replace(' ','')
    if last_first_name.count(' ')!=1:
        return False
    elif not name_without_space.isalpha():
        return False
    else:
        return True

def check_pin(pin):             #Перевірка Пін-коду ігрока на коректність вводу
    return pin.isdecimal()

def record_score(name, result): #Запис в файл результату Ігрока, якщо він кращий за попередній
    fh = open(r'C:\Users\PC\Desktop\Python\Part1\mybots\Scores.txt','r+',encoding='UTF-8')
    gamer_scores_for_record = fh.readlines()
    fh.close()
    current_record=int(gamer_scores_for_record[gamer_scores_for_record.index(name.title()+'\n')+2].replace('\n',''))
    if result>current_record:
        gamer_scores_for_record[gamer_scores_for_record.index(name.title()+'\n')+2]=str(result)+'\n'
        fh = open(r'C:\Users\PC\Desktop\Python\Part1\mybots\Scores.txt','w+', encoding='UTF-8')
        for i in gamer_scores_for_record:
            fh.write(i)
        fh.close()
    
def start(update, context):
    global alphabet_ukr, array_ukr_cities, cities_named, chair, attempt, circle_game, help_gamer, gamer_name, gamer_pin
    alphabet_ukr=[['а',0],['б',0],['в',0],['г',0],['д',0],['е',0],['є',0],['ж',0],['з',0],['и',0],['і',0],['ї',0],
            ['й',0],['к',0],['л',0],['м',0],['н',0],['о',0],['п',0],['р',0],['с',0],['т',0],['у',0],['ф',0],
            ['х',0],['ц',0],['ч',0],['ш',0],['щ',0],['ь',0],['ю',0],['я',0],[' ',0],["'",0],['-',0]]
    fh = open(r'C:\Users\PC\Desktop\Python\Part1\mybots\All_cities.txt', encoding="UTF-8")
    array_ukr_cities = fh.readlines()
    fh.close()
    format_array_ukr_cities ()
    init_alphabet_ukr ()
    cities_named = list ()      #зберігаються вже названі міста
    chair='початок'             #буква на яку потрібно назвати наступне місто
    attempt=0                   #кількість спроб
    circle_game=1               #коло гри
    help_gamer=0                #кількість підказок
    gamer_name=' '              #прізвище та ім'я ігрока
    gamer_pin='0000'            #пін-код ігрока
    context.bot.send_message(chat_id=update.effective_chat.id, text='Давай пограємо в дуже цікаву гру - МІСТА УКРАЇНИ -\n')
    context.bot.send_message(chat_id=update.effective_chat.id, text="Для старту гри потрібно зареєструвати Ігрока\n")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Введи свое Прізвище та Ім'я (бажано на українській мові) і пін-код\nЗразок: Шевченко Тарас 1234\n")
    return 1

def user (update, context):
    global gamer_name
    fh = open(r'C:\Users\PC\Desktop\Python\Part1\mybots\Scores.txt','r+',encoding='UTF-8')
    gamer_scores = fh.readlines()
    user_input=update.message.text
    gamer_name=user_input[:-5]
    gamer_pin=user_input[-4:]
    if not check_name(gamer_name) and not check_pin(gamer_pin):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Введіть правильно Прізвище та І'мя, а також пін-код")
    elif not check_name(gamer_name):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Введіть правильно Прізвище та І'мя")
    elif not check_pin(gamer_pin):
        context.bot.send_message(chat_id=update.effective_chat.id, text='Введіть правильно пін-код')
    elif gamer_name.title()+'\n' in gamer_scores and gamer_scores[gamer_scores.index(gamer_name.title()+'\n')+1]!=gamer_pin+'\n':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Ігрок з таким Прізвищем та І'мям вже існує, введіть іншe ПІ\nабо якщо це саме Ви, введіть вірний пін-код")
    else:
        if gamer_name.title()+'\n' in gamer_scores and gamer_scores[gamer_scores.index(gamer_name.title()+'\n')+1]==gamer_pin+'\n':
            context.bot.send_message(chat_id=update.effective_chat.id, text='Ласкаво просимо до гри '+gamer_name.title()+'. Ваш кращий результат: '+gamer_scores[gamer_scores.index(gamer_name.title()+'\n')+2])
        else:
            print(gamer_name.title(),file=fh)
            print(gamer_pin,file=fh)
            print('0',file=fh)
            context.bot.send_message(chat_id=update.effective_chat.id, text='Ласкаво просимо до гри '+gamer_name.title()+'. Ви граєте перший раз, тому нагадуємо\n прочитати правила ги - /rules подивитесь топ-20 результатів - /scores\nпідказка від ШІ - /help остановити гру - /stop')
        context.bot.send_message(chat_id=update.effective_chat.id, text='Почнемо гру...\n')
        fh.close()
        context.bot.send_message(chat_id=update.effective_chat.id, text='Введіть будь-яке українське місто:\n')
        return 2

def city_play(update, context):
    global circle_game, chair, attempt, help_gamer, gamer_name
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
        context.bot.send_message(chat_id=update.effective_chat.id, text='Ти ввів СТОП, що означає закінчення гри')
        context.bot.send_message(chat_id=update.effective_chat.id, text='Твій результат: -'+str(circle_game-help_gamer)+'-\nНе засмучуйся, наступного разу буде краще')
        record_score(gamer_name,(circle_game-help_gamer))
        return 3
    elif city in cities_named:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Таке місто вже називали'+end_string)
    elif city not in array_ukr_cities:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Такого міста в Україні не існує'+end_string)      
    elif chair!=city[0] and chair != 'початок':
        txt = 'Треба ввести місто назва якого починається з букви - '+chair.capitalize()+' -,а не з букви - '+city[0].capitalize()+' - '+end_string
        context.bot.send_message(chat_id=update.effective_chat.id, text=txt)
    else:
        attempt=0
        circle_game+=1
        chair=find_next_chair(city)
        if chair=='':
            context.bot.send_message(chat_id=update.effective_chat.id, text='У мене не залишилось варіантів назвати місто. ТИ ВИГРАВ!!!!!')
            context.bot.send_message(chat_id=update.effective_chat.id, text='Твій результат: -'+str(circle_game-help_gamer+100)+'-\nТИ ДУЖЕ КРУТИЙ - ВІТАЮ!!!!!')
            record_score(gamer_name,(circle_game-help_gamer+100))
            return 3
        context.bot.send_message(chat_id=update.effective_chat.id, text='Мені потрібно назвати місто на букву -'+chair.capitalize()+'-')
        city=computer_algorithm_generate_city(chair)
        context.bot.send_message(chat_id=update.effective_chat.id, text='Я називаю місто: '+city.capitalize())
        chair=find_next_chair(city)
        if chair=='':
            context.bot.send_message(chat_id=update.effective_chat.id, text='У тебе не залишилось варіантів назвати місто. Я виграв')
            context.bot.send_message(chat_id=update.effective_chat.id, text='Твій результат: -'+str(circle_game-help_gamer)+'-\nНе засмучуйся, наступного разу буде краще')
            record_score((gamer_name,circle_game-help_gamer))
            return 3
        context.bot.send_message(chat_id=update.effective_chat.id, text='КОЛО -'+str(circle_game)+' -') 
        context.bot.send_message(chat_id=update.effective_chat.id, text='Тобі потрібно назвати місто на букву: -'+chair.capitalize()+'-')
    if attempt==3:
        context.bot.send_message(chat_id=update.effective_chat.id, text='На жаль ти зробив 3 невірні спроби поспіль, що озачає програш')
        context.bot.send_message(chat_id=update.effective_chat.id, text='Твій результат: -'+str(circle_game-help_gamer)+'-\nНе засмучуйся, наступного разу буде краще...')
        record_score(gamer_name,(circle_game-help_gamer))
        return 3

def stop (update, context):  
    context.bot.send_message(chat_id=update.effective_chat.id, text='Ти ввів СТОП, що озачає закінчення гри')
    context.bot.send_message(chat_id=update.effective_chat.id, text='Твій результат: -'+str(circle_game-help_gamer)+'-\nНе засмучуйся, наступного разу буде краще...')
    record_score(gamer_name,(circle_game-help_gamer))
    return ConversationHandler.END

def rules (update, context):
    txt1 = '                   ПРАВИЛА ГРИ -МІСТА УКРАЇНИ- (ШІ-Штучний інтелект)\n'
    txt2 = '     1. Міста повинні бути тільки українськими та вводяться українською мовою.\n'
    txt3 = '     2. Введення назв сел, селищ та селищ міського типу не допускається.\n'
    txt4 = "     3. Спочатку Ігрок реєструється командою /start (бажано ввести своє Ім'я та Прізвище)\n"
    txt5 = '     4. У Ігрока є три спроби назвати місто. Якщо всі спроби хибні, то він програє.\n'
    txt6 = "     5. У Ігрока є три підказки від ШІ. Щоб цим скористатися треба ввести /help\n"
    txt7 = '     6. Наступне місто треба назвати на останню букву міста яке тільки що називалося.\n'
    txt8 = "     7. Якщо таких міст не існує, ШІ автоматично бере передостанню букву, і так далі.\n"
    txt9 = '     8. Гра закінчується, якщо неможливо назвати наступне місто перебираючи всі букви названого міста.\n'
    txt10 = '     9. Ігрок може закінчити ігру примусово, ввівши команду /stop .Для нової гри треба ввести /start\n'
    txt11 = '     10. Результат Ігрока це: Номер КОЛА - Число Підказок + 100 балів за виграш у ШІ.\n'
    txt12 = '     11. Всі результати зберігаються. Кращі 20 результатів можно вивести командою /scores.\n'
    txt13 = '                       - БАЖАЄМО ПЕРЕМОГИ, СЛАВА УКРАЇНІ!!! -\n'
    context.bot.send_message(chat_id=update.effective_chat.id, text=txt1+txt2+txt3+txt4+txt5+txt6+txt7+txt8+txt9+txt10+txt11+txt12+txt13)

def scores (update, context):
    fh = open(r'C:\Users\PC\Desktop\Python\Part1\mybots\Scores.txt','r+',encoding='UTF-8')
    gamer_scores_read = fh.readlines()
    fh.close()
    del gamer_scores_read[1::3]
    gamer_scores_for_print=[[0 for y in range (2)] for x in range(int(len(gamer_scores_read)/2))]
    for x in range(int(len(gamer_scores_read)/2)):
        gamer_scores_for_print[x][1]=(gamer_scores_read[x*2].replace('\n',''))
        gamer_scores_for_print[x][0]=int(gamer_scores_read[x*2+1].replace('\n',''))
    gamer_scores_for_print=sorted(gamer_scores_for_print, reverse=True)
    print_string_max=len(gamer_scores_for_print)
    if print_string_max>20:
        print_string_max=20
    context.bot.send_message(chat_id=update.effective_chat.id, text='     РЕКОРДИ ГРИ - МІСТА УКРАЇНИ -')  
    for x in range(print_string_max):
        context.bot.send_message(chat_id=update.effective_chat.id, text=str(gamer_scores_for_print[x][0])+'  '+gamer_scores_for_print[x][1])

def help (update, context): 
    global help_gamer
    end_string='' 
    if help_gamer==3:
        update.message.reply_text('На жаль ти вичерпав всі три підказки')
    elif circle_game==1:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Ще занадто рано для підказки')
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
        context.bot.send_message(chat_id=update.effective_chat.id, text='Підказка: спробуй ввести місто -'+city_help.capitalize()+'-\n'+end_string)

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
            3:  [CommandHandler('stop', stop)],
          },
          fallbacks=[CommandHandler('start', start)]
    )    

    dispatcher.add_handler(user_handler) 
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()