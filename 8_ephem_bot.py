"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""

from emoji import emojize
from glob import glob
import logging
from random import randint, choice
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import ephem, datetime


dt_now = datetime.date.today()
today_date = dt_now.strftime('%Y/%m/%d')


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO, 
                    filename='bot.log')


def greet_users(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    smile = context.user_data['emoji']
    message = f'Здравствуй! {smile}'
    update.message.reply_text(message)


def question_user(update, context):
    text = 'Введите название планеты на английском:'
    update.message.reply_text(text)


def const_print(update, user_planet):
    const_user_planet = ephem.constellation(user_planet(today_date))
    update.message.reply_text(const_user_planet)


def chek_to_planet(update, context):
    user_text = update.message.text.split()

    if 'Mercury' in user_text:
        user_planet = ephem.Mercury
    elif 'Venus' in user_text:
        user_planet = ephem.Venus
    elif 'Earth' in user_text:
        return update.message.reply_text('Наша планета не отображается для нас на небе, поэтому не может находиться в каком-либо созвездии))')
    elif 'Mars' in user_text:
        user_planet = ephem.Mars
    elif 'Jupiter' in user_text:
        user_planet = ephem.Jupiter
    elif 'Saturn' in user_text:
        user_planet = ephem.Saturn
    elif 'Uranus' in user_text:
        user_planet = ephem.Uranus
    elif 'Neptune' in user_text:
        user_planet = ephem.Neptune
    else:
        return update.message.reply_text('Не правильное написанние или это не планета. Напоминание: название планеты должно быть на английском и с заглавной буквы.')

    return const_print(update, user_planet)


def text_user(update, context):
    numb = len(update.message.text.split(" ")) - 1
    print(numb)
    text = f'{numb} слово(а)'
    update.message.reply_text(text)


def guees_numb(update, context):
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random_numbers(user_number,context)
        except(TypeError, ValueError):
            message = 'Введите целое число'
    else:
        message =  'Введите число'
    update.message.reply_text(message)


def play_random_numbers(user_number, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    smile = context.user_data['emoji']
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        message = f'Ваше число {user_number}, моё число {bot_number}, вы выиграли {smile}'
    elif user_number == bot_number:
        message = f'Ваше число {user_number}, моё число {bot_number}, ничья {smile}'
    else:
        message = f'Ваше число {user_number}, моё число {bot_number}, вы проиграли {smile}'
    return message


def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile)
    return user_data['emoji']


def send_cat_picture(update, context):
    cat_photo_list = glob('images/cat*.jp*g')
    cat_photo_filename = choice(cat_photo_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_photo_filename, 'rb'))


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('greet', greet_users))
    dp.add_handler(CommandHandler('planet', question_user))
    dp.add_handler(CommandHandler('wordcount', text_user))
    dp.add_handler(CommandHandler('guees', guees_numb))
    dp.add_handler(CommandHandler('cat', send_cat_picture))
    dp.add_handler(MessageHandler(Filters.text, chek_to_planet))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()