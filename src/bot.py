import os
import telebot


# Initialize bot
bot = telebot.TeleBot(
    os.environ['NASHENAS_BOT_TOKEN'], parse_mode='HTML'
)
