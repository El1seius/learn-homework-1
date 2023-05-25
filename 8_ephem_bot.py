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
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import ephem, datetime


dt_now = datetime.date.today()
today_date = dt_now.strftime('%Y/%m/%d')


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO, 
                    filename='bot.log')


def greet_user(update, context):
    text = 'Здравствуй!'
    update.message.reply_text(text)


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
        return const_print(update, user_planet)
    elif 'Venus' in user_text:
        user_planet = ephem.Venus
        return const_print(update, user_planet)
    elif 'Earth' in user_text:
        return update.message.reply_text('Наша планета не отображается для нас на небе, поэтому не может находиться в каком-либо созвездии))')
    elif 'Mars' in user_text:
        user_planet = ephem.Mars
        return const_print(update, user_planet)
    elif 'Jupiter' in user_text:
        user_planet = ephem.Jupiter
        return const_print(update, user_planet)
    elif 'Saturn' in user_text:
        user_planet = ephem.Saturn
        return const_print(update, user_planet)
    elif 'Uranus' in user_text:
        user_planet = ephem.Uranus
        return const_print(update, user_planet)
    elif 'Neptune' in user_text:
        user_planet = ephem.Neptune
        return const_print(update, user_planet)
    else:
        return update.message.reply_text('Не правильное написанние или это не планета. Напоминание: название планеты должно быть на английском и с заглавной буквы.')


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", question_user))
    dp.add_handler(MessageHandler(Filters.text, chek_to_planet))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()