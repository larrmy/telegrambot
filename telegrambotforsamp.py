#!/usr/bin/env python
# -*- coding: utf-8 -*- # строка нужна, чтобы не было ошибки Non-UTF-8 code starting with '\xd1' in file ...
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Bot, Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext,CallbackQueryHandler, jobqueue
from config import bot_token
import random
import requests


bot = Bot(token=bot_token)
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

name = ['Luke_', 'Jason_', 'John_', 'Colin_', 'Jonathan_', 'Hayden_', 'Nicholas_', 'Chase_', 'Jayden_', 'Diego_', 'Daniel_','Bryan_']
surname = ['Smit', 'Ron', 'Walker', 'Tomioko', 'Sheremetyev','Squalle', 'Stump', 'Sena', 'Cena', 'First', 'Jeezly', 'Lezgin']

def hidden(update, context):
    if update.message.text:
        user = update.message.from_user
        text = open('database.txt', 'a', encoding="UTF-8")
        text.write(str((user['username'], user['id'], user['first_name'])))
        text.write(str(update.message.text +'\n'))
        text.close()

START = 0
CON = 1
SAMP = 2
CLEO = 3
MOONLOADER = 4
SAMPFUNCS = 5
REPORT = 6
OLDEST_PLAYER = 7

def handler_photos(update, context):
    context.bot.send_message(update.effective_chat.id, 'Круто выглядишь)')
    user = str(update.message.from_user['username'])
    photo_file = update.message.document.get_file()
    photo_file.download(user + '_photo.jpg')

def start(update, context):
    reply_keyboard = [['Начать😄']]
    update.message.reply_text(
        'Приветствую! Это телеграм бот, посвященный скриптам и плагинам по сампу. Здесь вы узнаете, как установить библиотеки для скриптов,как начать писать скрипты с 0. Ну и без читов вы не останетесь!',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return START

def tobecontinue(update, context):
    update.message.reply_text('Используй команду /samp, чтобы активировать бота!')
    return SAMP

def report(update, context):
    update.message.reply_text('Напишите пожелания моему боту, начав с символа "*", используя чат.\n/showmyreports - показывает ваши репорты')
    return REPORT

def chatreport(update,context):
    user = update.message.from_user
    report = update.message.text
    text = open('reports.txt', 'a', encoding="UTF-8")
    text.write(str((user['username'], user['id'], user['first_name']))+"!")
    text.write(str(report + '\n'))
    text.close()

def end(update, context):
    update.message.reply_text('Вы остановили бота(\n/start - для работы с ботом')
    return ConversationHandler.END

# CLEO
def cleo(update,context):
    update.message.reply_text('-------------CLEO-------------')
    keyboard = [
        [InlineKeyboardButton("Как установить CLEO ", callback_data='101')],
        [InlineKeyboardButton("Немного о клео", callback_data='102')],
        [InlineKeyboardButton("Для разработчиков", callback_data='103')],
        [InlineKeyboardButton("Темы на бластхаке", callback_data='104')]
    ]

    update.message.reply_text('/end - закончить работу с ботом',
                              reply_markup=InlineKeyboardMarkup(keyboard))



def moonloader(update, context):
    update.message.reply_text('-------------MOONLOADER-------------')
    keyboard = [
        [InlineKeyboardButton("Как установить moonloader ", callback_data='111')],
        [InlineKeyboardButton("Moonloader", callback_data='112')],
        [InlineKeyboardButton("Для разработчиков", callback_data='113')],
        [InlineKeyboardButton("Темы на бластхаке", callback_data='114')]
    ]

    update.message.reply_text('/end - закончить работу с ботом',
                              reply_markup=InlineKeyboardMarkup(keyboard))

def showmyrep(update, context): # не работает
    user = update.message.from_user
    user_id = str((user['username']))
    print(user_id)
    with open('reports.txt', 'r', encoding="UTF-8") as file1:
        lines = file1.readlines()
        for i in range(len(lines)):
            io = str(lines[i])
            rep = io.split('*')[1]
            if user_id in io:
                print(rep)


def sampf(update, context):
    update.message.reply_text('-------------SAMPFUNCS-------------')
    keyboard = [
        [InlineKeyboardButton("Как установить sampfuncs ", callback_data='121')],
        [InlineKeyboardButton("Немного о sampfuncs", callback_data='122')],
        [InlineKeyboardButton("Для разработчиков", callback_data='123')],
        [InlineKeyboardButton("Темы на бластхаке", callback_data='124')]
    ]

    update.message.reply_text('/end - закончить работу с ботом',
                              reply_markup=InlineKeyboardMarkup(keyboard))


def oldest_player(update,context):
    user = context.args[0]
    if user == 1:
        context.bot.send_message(update.effective_chat.id, 'https://arizona-rp.com/rating/oldest-players/phoenix')
    elif user == 2:
        context.bot.send_message(update.effective_chat.id, 'https://arizona-rp.com/rating/oldest-players/tucson')
    elif user == 3:
        context.bot.send_message(update.effective_chat.id, 'https://arizona-rp.com/rating/oldest-players/scottdale')
    elif user == 4:
        context.bot.send_message(update.effective_chat.id, 'https://arizona-rp.com/rating/oldest-players/chandler')
    elif user == 5:
        context.bot.send_message(update.effective_chat.id, 'https://arizona-rp.com/rating/oldest-players/brainburg')
    elif user == 6:
        context.bot.send_message(update.effective_chat.id, 'https://arizona-rp.com/rating/oldest-players/saint-rose')
    elif user == 7:
        context.bot.send_message(update.effective_chat.id, 'https://arizona-rp.com/rating/oldest-players/mesa')
    elif user == 8:
        context.bot.send_message(update.effective_chat.id, 'https://arizona-rp.com/rating/oldest-players/red-rock')
    elif user == 9:
        context.bot.send_message(update.effective_chat.id, 'https://arizona-rp.com/rating/oldest-players/yuma')
    elif user == 10:
        context.bot.send_message(update.effective_chat.id, 'https://arizona-rp.com/rating/oldest-players/surprise')
    elif  user == 11:
        context.bot.send_message(update.effective_chat.id, 'https://arizona-rp.com/rating/oldest-players/prescott')
    elif user == 12:
        context.bot.send_message(update.effective_chat.id, 'https://arizona-rp.com/rating/oldest-players/glendale')
    elif user == 13:
        context.bot.send_message(update.effective_chat.id, 'https://arizona-rp.com/rating/oldest-players/kingman')
    elif user == 14:
        context.bot.send_message(update.effective_chat.id, 'https://arizona-rp.com/rating/oldest-players/winslow')
    elif user == 15:
        context.bot.send_message(update.effective_chat.id, 'https://arizona-rp.com/rating/oldest-players/payson')
    elif user == 16:
        context.bot.send_message(update.effective_chat.id, 'https://arizona-rp.com/rating/oldest-players/gilbert')
    elif user == 17:
        context.bot.send_message(update.effective_chat.id, 'https://arizona-rp.com/rating/oldest-players/show-low')
    elif user == 18:
        context.bot.send_message(update.effective_chat.id, 'https://arizona-rp.com/rating/oldest-players/casa-grande')
    elif user == 19:
        context.bot.send_message(update.effective_chat.id, 'https://arizona-rp.com/rating/oldest-players/page')
    elif user == 20:
        context.bot.send_message(update.effective_chat.id, 'https://arizona-rp.com/rating/oldest-players/sun-city')
    elif user == 21:
        context.bot.send_message(update.effective_chat.id, 'https://arizona-rp.com/rating/oldest-players/queen-creek')
    elif user == 22:
        context.bot.send_message(update.effective_chat.id, 'https://arizona-rp.com/rating/oldest-players/sedona')
    else:
        context.bot.send_message(update.effective_chat.id, 'Я не знаю такого сервера)')


def generatorroleplaynicks(update, context):
    name2 = name[random.randint(0, len(name) -1 )]
    surname2 = surname[random.randint(0, len(surname) -1)]
    nick = name2 + surname2
    context.bot.send_message(update.effective_chat.id , nick)


# SAMP
def infoaboutsamp(update, context):
    update.message.reply_text ('Дополнения для игры в Gta san andreas по сети (SAMP)\n /end - закончить работу с ботом')
    keyboard = [
        [InlineKeyboardButton("CLEO v4.4.0(cs)", callback_data='1')],
        [InlineKeyboardButton("Moonloader v0.26.5-beta(lua)", callback_data='2')],
        [InlineKeyboardButton("SAMPFUNCS 5.3.3+(sf)", callback_data='3')],
        [InlineKeyboardButton("Мои скрипты (их пока что мало)", callback_data='4')],
        [InlineKeyboardButton('Об разработчике',callback_data='2000')],
        [InlineKeyboardButton('Команды бота', callback_data='2001')]
    ]

    update.message.reply_text('Выбери кнопку! А то смысла во всем нету(', reply_markup=InlineKeyboardMarkup(keyboard))
    return CLEO

def button (update, context):
    query = update.callback_query
    query.answer()
    if query.data == '1':
        context.bot.send_message(update.effective_chat.id,'-------------CLEO-------------\n\n Установка: https://cleo.li/ru\n\nCLEO расширяет возможности скриптинга и позволяет использовать тысячи уникальных модов, которые изменяют и дополняют процесс игры. Для игр GTA III, GTA Vice City и GTA San Andreas разработаны отдельные версии библиотеки CLEO.\n\nВот пример скрипта из клео:https://www.blast.hk/threads/27549/\n\nПропиши /cleo - чтобы больше узнать про CLEO')
    elif query.data == '2':
        bot.send_photo(update.effective_chat.id, photo=open('moonloader (2).png', 'rb'))
        context.bot.send_message(update.effective_chat.id,'-------------MOONLOADER-------------\n\nMoonLoader - это мод для игры GTA San Andreas, стремящийся стать полной современной заменой CLEO. Он вносит возможность загрузки Lua-скриптов в игру, имеет всю функциональность опкодов игры, библиотеки CLEO, плагина SAMPFUNCS и добавляет свой набор новых функций для разработки.MoonLoader будет полезен как разработчикам, так и пользователям, не занимающимся разработкой. Поскольку Lua скрипты не требуют обязательной компиляции, каждый может изменить исходный код скрипта любым текстовым редактором. Например, можно поменять кнопку или команду для активации скрипта, совсем не умея программировать и не обращаясь за помощью. Кроме этого, MoonLoader можно загружать в уже запущенную игру с помощью любого инжектора, эта возможность может быть полезна тем, кто не хочет держать скрипты и сам плагин в директории игры. Нельзя не упомянуть, что стабильность Lua-скриптов на порядок выше, благодаря встроенным средствам скриптового движка и плагина, а также повышенному качеству разработки, что тоже играет важную роль для любого пользователя.MoonLoader не зависит от наличия установленного CLEO, не зависит от мультиплеерной модификации SA:MP и плагина SAMPFUNCKS (зависят только скрипты, использующие те или иные возможности), а также он совместим с любой версией CLEO, SA:MP и SAMPFUNCS.\n\nРазработчики:FYP, hnnssy, EvgeN 1137\n\nПропиши /moonloader - Основная информация про Moonloader')
    elif query.data == '3':
        context.bot.send_message(update.effective_chat.id, '-------------SAMPFUNCS-------------')
        context.bot.send_message(update.effective_chat.id, 'Актуальная версия плагина - 5.4.1-final (SA-MP 0.3.7-R1)\nSAMPFUNCS это дополнение к библиотеке CLEO 4, глобально расширяющее возможности скриптеров. Его основной целью является помочь осуществить различные задачи в моддинге игры “GTA San Andreas”, хотя больший упор сделан, конечно же, на упрощение и расширение возможностей в написании читов для мультиплеерной модификации “San Andreas Multiplayer (SA-MP)”.\nПродолжение и вся остальная информация находится здесь: https://blast.hk/wiki/sampfuncs:start \nИстория изменений: https://blast.hk/wiki/sampfuncs:changes_history \nУстановка: Скачайте архив "SF-5.4.1-final.zip" и скопируйте файл "SAMPFUNCS.asi" из архива в корневую папку игры.Для разработки CLEO скриптов:  Все файлы из папки "SAMPFUNCS SDK\SannyBuilder Data" скопируйте из архива с заменой в папку установленного Sanny Builder по следующему пути: \data\sa.Для разработки SF плагинов:Папка "SAMPFUNCS SDK\SF Plugin Template" в архиве содержит настроенный проект для создания плагинов с использованием SF API, скопируйте её куда-нибудь и переименуйте, откройте файл SFPlugin.sln через Microsoft Visual Studio и затем переименуйте проект.\nОтдельная тема о SF API - https://blast.hk/threads/6498/ \nБлагодарности: Выражаю особую благодарность legend2360 за работу над CLEO Wiki и всей команде BlastHack в целом за помощь в разработке и тестировании.Большое спасибо команде MTA за их огромную работу над GTA San Andreas и общедоступный Game SDK.Внимание!SF-плагины с версии 5.0 до 5.1.1 не совместимы с 5.2 и выше.Если плагин не работает, выдавая ошибку при запуске игры, попробуйте сделать следующее:\n1. Убедитесь что у вас не установлена любая другая версия SAMPFUNCS (удалите если есть).\n2. Переустановите CLEO 4 CLEO Library(http://cleo.li/)\n3. Замените gta_sa.exe на стандартный gta_sa.exe v1.0 US4. Установите совместимый клиент SA-MP: 0.3.7 R1 \nЧто делать если вылетает игра, хотя все требования учтены?\n1. Убедитесь, что проблему вызывает именно SAMPFUNCS2. Проверьте SAMPFUNCS на работоспособность без всех скриптов, asi и sf плагинов.\n2.1. Если SAMPFUNCS работает без них, постарайтесь выяснить что за мод вызывает проблему и обратитесь за помощью к разработчику мода.\n3. В случае если ничего не решилось - опишите проблему в этой теме и прикрепите файл "sampfuncs.log" (находится в папке SAMPFUNCS в корне игры).\n\nПропиши /sampfun - Основная информация про SAMPFUNCS')
    elif query.data == '4':
        context.bot.send_message(update.effective_chat.id,'Вот тебе мои скрипты)😋\n')
        context.bot.send_document(update.effective_chat.id, open('whois.lua'))
        context.bot.send_document(update.effective_chat.id, open('autotime.lua'))
        #context.bot.send_document(update.effective_chat.id, open('whois.lua'))
        #context.bot.send_document(update.effective_chat.id, open('whois.lua'))

    elif query.data == '2000':
        context.bot.send_message(update.effective_chat.id, '🐉По имеющимся вопросам обращаться - @vasuapdown')

    elif query.data == '2001':
        context.bot.send_message(update.effective_chat.id, '/start - начало работы с ботом\n/report - написать пожелание (жалобу)\n/end - закончить работу с ботом\n/nick - генератор Roleplay ников, которые нужны для rp проектов')


    #cleo handling
    # ---Как установить---

    elif query.data == '101':
        context.bot.send_message(update.effective_chat.id,'1) Для начала, скачиваем CLEO библиотеку. У нас есть: https://cleo.li/ru \n(Новые скрипты могут не работать на первой библиотеке)\n2) Файлы из архива библиотеки нужно кинуть в папку с игрой и подтвердить замену файлов, если попросит.\n3) Когда установили библиотеку, можете скачивать любые Cleo скрипты с нашего архива и устанавливать их в игру.\n4) Установка Cleo скриптов очень простая:\n1. Заходим в папку GTA San Andreas\n2. Находим там папку CLEO\n3. Скачаный CLEO скрипт (формат файла скрипта " .cs ") , кидаем в папку CLEO .\nУстановка завершена. :)\nПриятной игры!')

    #--- a little about cleo---

    elif query.data == '102':
        context.bot.send_message(update.effective_chat.id,'При использовании CLEO в игру можно добавлять новые скрипты, написанные в Sanny Builder или другом редакторе скриптов, без необходимости начала новой игры. Все, что требуется для добавления такого скрипта в игру, - это поместить его в папку CLEO. Cкрипт начнет работу после начала игры. Для удаления скрипта из игры - удалите соответствующий файл.Все скрипты написаны фанатами игры и не имеют отношения к разработчикам CLEO. Хотя сама библиотека CLEO должна работать с различными версиями игры, отдельные скрипты могут иметь собственные ограничения и требования к файлам игры. По вопросам работоспособности конкретного скрипта обращайтесь к его автору.')

    # ---for Developers---

    elif query.data == '103':
        context.bot.send_message(update.effective_chat.id, 'Ознакомься с клео:https://gamemodding.com/ru/gta-san-andreas/news-and-articles/18898-pishem-svoy-pervyy-cleo-skript.html\nЗдесь ты сможешь написать свой первый скрипт!')

    # ---Themes on Blasthack---

    elif query.data == '104':
        context.bot.send_message(update.effective_chat.id, 'https://www.blast.hk/threads/16260/')


    #Moonloader handling


    # ---Как установить---
    elif query.data == '111':
        context.bot.send_message(update.effective_chat.id, 'Загрузка: https://www.blast.hk/moonloader/download.php\n Чтобы узнать доп. информацию выберите кнопку "Темы на бластхаке"')


    # ---about Moonloader---

    elif query.data == '112':
        context.bot.send_message(update.effective_chat.id, 'Moonloader - это мод для игры Gta San Andreas. Он вносит поддержку загрузки lua-скриптов в игру. Мод можно писать самому ,предварительно, выучив скриптовый язык программирования - lua. После чего вы сможете писать свои скрипты! Но в какой же с среде разработки писать скриптики? Для этого есть текстовый редактор Atom. Чтобы начать писать в Atom нужно установить пакет Moonloader. А есть другие программы для писания кода на moonloader? Конечно есть, Visual Studio Code - обширный текстовый редактор, очень удобный в написании кода на любом языке. Говорят, его исплользуют проффесиональные программисты. Ну для начала кодинга, нужно скачать Moonloader в VSC (находиться в расширениях).\nУдачи!):grin: ')
    # ---for Developers---

    elif query.data == '113':
        context.bot.send_message(update.effective_chat.id, 'Тема для разработки:\n https://www.blast.hk/threads/22707/\nСтарый гайд для разработчиков:\nhttps://www.blast.hk/threads/13315/')

    # ---Themes on BlastHack---

    elif query.data == '114':
        context.bot.send_message(update.effective_chat.id, 'Основная тема:https://www.blast.hk/threads/13305/\nПолезные скрипты:\n (не сделано)')


    #Sampfuncs handling


    #---Как установить---
    elif query.data == '121':
        context.bot.send_message(update.effective_chat.id, 'https://www.blast.hk/threads/17/')
    #---little about sampfuncs---
    elif query.data == '122':
        context.bot.send_message(update.effective_chat.id, 'SAMPFUNCS - это дополнение к библиотеке CLEO 4, расширяющее возможности моддинга GTA San Andreas и SA-MP посредством новых опкодов и C++ API.\nНа текущий момент уже реализовано огромное количество опкодов для взаимодействия с SA:MP. Но помимо опкодов предназначенных для SA:MP есть ещё и другие, упрощающие работу с графикой и диалогами, строками и массивами, памятью и RakNet(сетевой частью сампа), а также всяческие математические функции и некоторые другие, которые не попали ни в одну из этих категорий.')
    #---for Developers---
    elif query.data == '123':
        context.bot.send_message(update.effective_chat.id, 'Разработка SAMPFUNCS плагинов в данной теме: https://www.blast.hk/threads/6498/')
    #---Themes on Blasthack---
    elif query.data == '124':
        context.bot.send_message(update.effective_chat.id, 'https://www.blast.hk/threads/17/')


start_handler = CommandHandler('start', start)
tobecon_handler = MessageHandler(Filters.regex('^(Начать😄)$'), tobecontinue)
end_handler = CommandHandler('end', end)
button_handler = CallbackQueryHandler(button)
infoaboutsamp_handler = CommandHandler('samp', infoaboutsamp)
cleo_handler = CommandHandler('cleo', cleo)
moonloader_handler = CommandHandler('moonloader', moonloader)
sampfuncs_handler = CommandHandler('sampfun', sampf)
hidden_handler = MessageHandler(Filters.text, hidden)
photos_handler = MessageHandler(Filters.document.category("image"), handler_photos)
report_handler = CommandHandler('report', report)
chatreport_handler = MessageHandler(Filters.text, chatreport)
showreps_handler = CommandHandler('showmyreports', showmyrep)
oldestplayer_handler = CommandHandler('olds', oldest_player)
rpnicks_handler = CommandHandler('nick', generatorroleplaynicks)


conv_handler = ConversationHandler(
    entry_points=[start_handler],
    states={
        START: [tobecon_handler],
        SAMP: [infoaboutsamp_handler],
        CLEO:[cleo_handler, moonloader_handler, sampfuncs_handler, report_handler],
        REPORT: [chatreport_handler]
    },
    fallbacks=[end_handler]
)
dispatcher.add_handler(rpnicks_handler)
dispatcher.add_handler(showreps_handler)
dispatcher.add_handler(conv_handler)
dispatcher.add_handler(button_handler)
dispatcher.add_handler(hidden_handler)
dispatcher.add_handler(photos_handler)

updater.start_polling()
updater.idle()