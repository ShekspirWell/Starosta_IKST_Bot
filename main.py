import datetime
import telebot
import info
from format_xlsx import mainSchedule as sd
from format_xlsx import ciphersOfGroups
from format_xlsx import board_ciphers as bc
import check_in

bot = telebot.TeleBot(info.token)

print(bot.get_me())


@bot.message_handler(commands=['start'])  # Срабатывает при старте
def start(message):
    markup_course = telebot.types.ReplyKeyboardMarkup(True).row('1 курс', '2 курс').row('3 курс', '4 курс').row(
        '5 курс')
    bot.send_message(message.chat.id, 'Добро пожаловать.\nВыберите ваш курс:', reply_markup=markup_course)


@bot.message_handler(content_types=['text'])  # Срабатывает при получении текста
def comes_text(message):
    if message.text == '1 курс' or '2 курс' or '3 курс' or '4 курс':
        if message.text == '1 курс':
            make_markup(message, '1')
        if message.text == '2 курс':
            make_markup(message, '2')
        if message.text == '3 курс':
            make_markup(message, '3')
        if message.text == '4 курс':
            make_markup(message, '4')
        if message.text == '5 курс':
            make_markup(message, '5')

    if message.text == 'Какая пара?':
        ans_schedule(message)
    if message.text == 'Старостат':
        ans_schedule(message)

    for r in range(ciphersOfGroups.__len__()):
        if message.text == ciphersOfGroups[r]:
            check_in.registration(message.chat.id, message.text)

            markup_menu = telebot.types.ReplyKeyboardMarkup(True)
            markup_menu.row('Какая пара?').row('Старостат')
            bot.send_message(message.chat.id, 'Функции бота:', reply_markup=markup_menu)


def make_markup(message, course):
    markup_group = telebot.types.ReplyKeyboardMarkup(True)
    if bc[course].__len__() % 2 == 0:
        for btn in range(int((bc[course].__len__()) / 2)):
            markup_group.row(bc[course][btn * 2], bc[course][btn * 2 + 1])
        bot.send_message(message.chat.id, 'Выберите группу:', reply_markup=markup_group)
    else:
        for btn in range(int((bc[course].__len__() - 1) / 2)):
            markup_group.row(bc[course][btn * 2], bc[course][btn * 2 + 1])
        markup_group.row(bc[course][-1])
        bot.send_message(message.chat.id, 'Выберите группу:', reply_markup=markup_group)


def ans_schedule(message):
    now = datetime.datetime.now()
    day = now.weekday()
    print(message)
    if 0 <= day <= 4:
        time = now.time()
        t = time.hour.__float__() + time.minute.__float__() / 100
        if 0.01 < t <= 9.20:
            if now.isocalendar()[1] % 2 == 0:
                bot.send_message(message.chat.id, sd[check_in.get_user_cipher(message.chat.id)][0 + (day * 8)])
            else:
                bot.send_message(message.chat.id, sd[check_in.get_user_cipher(message.chat.id)][1 + (day * 8)])

        if 9.21 < t <= 10.50:
            if now.isocalendar()[1] % 2 == 0:
                bot.send_message(message.chat.id, sd[check_in.get_user_cipher(message.chat.id)][2 + (day * 8)])
            else:
                bot.send_message(message.chat.id, sd[check_in.get_user_cipher(message.chat.id)][3 + (day * 8)])

        if 10.51 < t <= 12.20:
            if now.isocalendar()[1] % 2 == 0:
                bot.send_message(message.chat.id, sd[check_in.get_user_cipher(message.chat.id)][4 + (day * 8)])
            else:
                bot.send_message(message.chat.id, sd[check_in.get_user_cipher(message.chat.id)][5 + (day * 8)])

        if 12.21 < t <= 14.00:
            if now.isocalendar()[1] % 2 == 0:
                bot.send_message(message.chat.id, sd[check_in.get_user_cipher(message.chat.id)][6 + (day * 8)])
            else:
                bot.send_message(message.chat.id, sd[check_in.get_user_cipher(message.chat.id)][7 + (day * 8)])
        if 14.01 < t <= 23.59:
            if now.isocalendar()[1] % 2 == 0:
                if day + 1 != 5 and day + 1 != 6:
                    bot.send_message(message.chat.id, sd[check_in.get_user_cipher(message.chat.id)][0 + ((day + 1) * 8)])
                else:
                    bot.send_message(message.chat.id, 'Завтра выходной')
            else:
                if day + 1 != 5 and day + 1 != 6:
                    bot.send_message(message.chat.id, sd[check_in.get_user_cipher(message.chat.id)][1 + ((day + 1) * 8)])
                else:
                    bot.send_message(message.chat.id, 'Завтра выходной')
    else:
        bot.send_message(message.chat.id, 'Сегодня выходной')


bot.polling(none_stop=True)
