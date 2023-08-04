import telebot
from telebot import types
import requests
import json
from bs4 import BeautifulSoup


api_token = '6600003289:AAEig0_NbSXFa_GXlgw16Z54DozQ_xwnJY4'


bot = telebot.TeleBot(api_token)

# создание опроса для выбора блюда
# bot.send_poll(chat_id=391434651, question='Какое блюдо Вы предпочитаете в качестве основного?',
#               options=['Мясное 🥩', 'Рыбное 🐟'], is_anonymous=False)


# стикеры
together = 'CAACAgIAAxkBAAEJ3pxkx-M_f4G1eKdxoTt3bP6UkninIwACCUYAAjlDQUrrnVgH8Q6wRS8E'
wineglass = 'CAACAgIAAxkBAAEJ3p5kx-NTvNCP4zb4t9t8F3MwCdGhLgACnzIAAvGYQEqM85bHwLkpDy8E'
rock = 'CAACAgIAAxkBAAEJ3qBkx-Ng_WZfa2VlSfbzXYnuKd5paQAC0DAAAjWwQErSe7JKO5Kyny8E'
fright = 'CAACAgIAAxkBAAEJ3qJkx-NzV3kfwB6rEtDC7OP1N14qPAACky4AAnnjQEp0m2uheQ88Yi8E'
hello = 'CAACAgIAAxkBAAEJ3qhkx-bHopEsgVIHmmjE6eWHfv1lgwACrzUAAnVAQErfakWAoZag6y8E'
kiss = 'CAACAgIAAxkBAAEJ3qZkx-a7BWIDkx_ACeFpIiub0qzO-QACO0UAAsK8QUq3RRKPO9l00C8E'
klass = 'CAACAgIAAxkBAAEJ3qpkx-bTH9zcxGma5r49PX3BpMs6lwACNjsAAmbvQEofIl1KW_4LVS8E'
car = 'CAACAgIAAxkBAAEJ3rlkx-qNDLSaEqtcESOTVpgnNC8ZiwACnjMAAgOXQEobjz2YI2BOGi8E'


# создание меню
markup = types.ReplyKeyboardMarkup(row_width=1)
item1 = types.KeyboardButton('Ключевые события дня 🎉')
item2 = types.KeyboardButton('План дня 🗓️')
item3 = types.KeyboardButton('Выбрать основное блюдо 🍴')
item4 = types.KeyboardButton('Дресс-код 👔')
item5 = types.KeyboardButton('Погода в день торжества ☀️')
item6 = types.KeyboardButton('Беседа 💬')
item7 = types.KeyboardButton('Важные контакты 📲')

markup.add(item1, item2, item3, item4, item5, item6, item7)

# наполнение разделов бота

# ключевые события дня
key_event = '<b>КЛЮЧЕВЫЕ СОБЫТИЯ ДНЯ</b>\n\n' \
            '👰🏻‍♀️🤵🏻 БРАКОСОЧЕТАНИЕ\n\n' \
            '⏰ Время: 11:00\n' \
            '🏰 Место: Дворец бракосочетания №1\n' \
            '📍 Адрес: г. Санкт-Петербург, Английская набережная, д. 28\n\n' \
            '⛵ ПРОГУЛКА НА ТЕПЛОХОДЕ\n\n' \
            '⏰ Время: 12:30 - 14:30\n' \
            '🛳️ Место отправления и прибытия: наб. Реки Фонтанки, д. 26\n\n' \
            '🥂 СВАДЕБНЫЙ БАНКЕТ\n\n' \
            '⏰ Время: 15:00\n' \
            '🏨 Место: банкетный зал "Boutique Hall"\n' \
            '📍 Адрес: г. Санкт-Петербург, наб. реки Пряжки, д. 5'

# план дня
schedule = '<b>ПЛАН ДНЯ</b>\n\n' \
           '🕥 10:45 - Сбор гостей у ЗАГСа\n\n' \
           '🕚 11:00 - 11:30 - Торжественная церемония\n\n' \
           '🕦 11:30 - 12:30 - Фото с молодоженами и время добраться до причала теплохода\n\n' \
           '🕧 12:30 - 14:30 - Водная прогулка по рекам и каналам, фуршет\n\n' \
           '🕑 14:30 - 15:00 - Время добраться до банкета\n\n' \
           '🕒 15:00 - Свадебное торжество\n\n' \
           '🕕 18:30 - Торт\n\n' \
           '🕖 19:00 - Завершение программы, свадебные огни\n\n' \
           '🌃 До 21:00 - Афтерпати, дискотека.'

# дресс-код
dress_code = '<b>ДРЕСС-КОД</b>\n\n' \
             'Мы ценим ваше внимание к свадебному торжеству и хотели бы сделать его особенным для всех гостей. ' \
             'У нас нет жёстких ограничений в дресс-коде, но мы просим вас по возможности избегать некоторых ' \
             'элементов одежды.\n\n' \
             '🚫 Пожалуйста, избегайте:\n' \
             '• Белых нарядов\n' \
             '• Джинсов и спортивной одежды\n\n' \
             'Выберите наряды, которые подчеркнут вашу индивидуальность, создадут праздничное и ' \
             'элегантное настроение, а также добавят чудесный штрих к нашему сказочному моменту.'

# чат для гостей
chat = '<b>БЕСЕДА</b>\n\n' \
       '🎊 Дорогие гости!\n\n' \
       '📸 Мы бы хотели сохранить как можно больше памятных моментов с нашего торжества, ' \
       'поэтому хотели бы видеть созданные вами фото- и видео- шедевры в беседе свадьбы.\n\n' \
       '🎈 Общайтесь с другими гостями и делитесь радостью и пожеланиями для молодоженов\n\n' \
       'https://t.me/+JeThD20tLiEzMzcy'

# контакты
contacts = '<b>ВАЖНЫЕ КОНТАКТЫ</b>\n\n' \
           '🕺 Если у Вас появились какие-либо творческие предложения, ' \
           'то можете смело писать нашему ведущему Александру:\n' \
           '+7 (999) 212-14-09\n\n ' \
           '👩🏻‍💼 По организационным вопросам можно обратиться к координатору Алле:\n' \
           '+7 (921) 937-19-89'


@bot.message_handler(commands=['start'])
def hello(message):
    return bot.send_message(message.chat.id, text=f'Привет, {message.from_user.full_name}!❤️\n\n'
                                                  f'Выберите интересующий Вас раздел в меню:', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def message_reply(message):

    if message.text == 'Ключевые события дня 🎉':
        return bot.send_message(message.chat.id, key_event, parse_mode='HTML'), \
               bot.send_sticker(message.chat.id, car)
    elif message.text == 'Выбрать основное блюдо 🍴':
        return bot.forward_message(message.chat.id, 391434651, 296), \
               bot.send_sticker(message.chat.id, wineglass)
    elif message.text == 'План дня 🗓️':
        return bot.send_message(message.chat.id, schedule, parse_mode='HTML'), \
               bot.send_sticker(message.chat.id, kiss)
    elif message.text == 'Дресс-код 👔':
        return bot.send_message(message.chat.id, dress_code, parse_mode='HTML'), \
               bot.send_sticker(message.chat.id, rock)
    elif message.text == 'Беседа 💬':
        return bot.send_message(message.chat.id, chat, parse_mode='HTML'), \
               bot.send_sticker(message.chat.id, klass)
    elif message.text == 'Погода в день торжества ☀️':
        return bot.send_message(message.chat.id, weather(), parse_mode='HTML')
    elif message.text == 'Важные контакты 📲':
        return bot.send_message(message.chat.id, contacts, parse_mode='HTML')


def weather():
    r = requests.get('https://pogoda.365c.ru/russia/sankt_peterburg/d/16-avgusta')

    soup = BeautifulSoup(r.text, 'html.parser')

    # temperature - средняя температура днем
    temperature_data = soup.find_all('div', {'class': 'temp'})
    temperature_sort = [i.text for i in temperature_data]
    temperature = temperature_sort[0][:-1]

    # давление, влажность, ветер, вероятность осадков
    weather_data = soup.find_all('div', {'class': 'leftcol'})
    weather_sort = [i.text for i in weather_data]

    pressure = weather_sort[0]
    humidity = weather_sort[1]
    wind_value = weather_sort[2][-10:-5]
    rain = weather_sort[3]

    # определение количества осадков

    # if rain_mm < 0.5:
    #     rain = 'не ожидаются'
    # elif 1 < rain_mm < 5:
    #     rain = 'слабые'
    # elif 5 < rain_mm < 15:
    #     rain = 'умеренные'
    # elif 15 < rain_mm < 25:
    #     rain = 'сильные'
    # else:
    #     rain = 'очень сильные'

    # определение силы ветра

    # if wind_value < 5:
    #     wind = 'слабый'
    # elif 5 < wind_value < 15:
    #     wind = 'умеренный'
    # elif 15 < wind_value < 25:
    #     wind = 'сильный'
    # else:
    #     wind = 'очень сильный'

    return f'<b>ПОГОДА 16 АВГУСТА</b>\n'\
           f'Санкт-Петербург\n\n'\
           f'🌡️ Средняя температура днем:  {temperature}°C\n\n'\
           f'🌧️ {rain[:19]}: {rain[19:]}\n\n'\
           f'💨 Сила ветра: {wind_value}\n\n'\
           f'💧 {humidity[:17]}: {humidity[17:]} \n\n'\
           f'☁️ {pressure[:8]}: {pressure[8:]}\n\n'


bot.infinity_polling()


bot.polling(none_stop=True)


# url = 'https://api.telegram.org/bot6600003289:AAEig0_NbSXFa_GXlgw16Z54DozQ_xwnJY4/getupdates'
#
# response = requests.get(url)
# print(response.text)
