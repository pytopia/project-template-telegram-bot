import os

import telebot
from loguru import logger

from src.constants import keyboards
from src.utils.io import write_json


class Bot:
	"""
	Template for telegram bot.
	"""
	def __init__(self):
		self.bot = telebot.TeleBot(os.environ['NASHENAS_BOT_TOKEN'])
		self.echo_all = self.bot.message_handler(
			func=lambda message: True
		)(self.echo_all)

	def run(self):
		logger.info('Bot is running...')
		self.bot.infinity_polling()

	def echo_all(self, message):
		write_json(message.json, 'messages.json')
		self.bot.send_message(
			message.chat.id, message.text,
			reply_markup=keyboards.main
		)


if __name__ == '__main__':
	logger.info('Bot started')
	bot = Bot()
	bot.run()
