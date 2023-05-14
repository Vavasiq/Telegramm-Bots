import telebot

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config

owm = OWM('b59fa188c58b2be1bfe9b87d7cb2a736')

config_dict = get_default_config()
config_dict['language'] = 'ru'

bot = telebot.TeleBot("1973052569:AAHJmDQsEDnyEaHGWRXzSOnp9VSSr3uoEZM")

mgr = owm.weather_manager()


@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = mgr.weather_at_place(message.text)
	w = observation.weather
	temp = w.temperature('celsius')["temp"]
	answer = "В городе " + message.text + " сейчас " + w.detailed_status +"\n"
	answer += "Температура около: " + str(temp) +"\n\n"
	if temp<10:
		answer += "Не отморозь бубенчики"
	bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True )
