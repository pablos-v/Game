from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import commands as c
import my_bot_api



updater = Updater(my_bot_api.api) # Создайте файл my_bot_api.py(добавлен в игнор) и в переменную api положите ваш код
print("Server started")

updater.dispatcher.add_handler(CommandHandler('help', c.help))
updater.dispatcher.add_handler(CommandHandler('run', c.run))
updater.dispatcher.add_handler(CommandHandler('turn', c.turn))
updater.dispatcher.add_handler(MessageHandler(Filters.command, c.unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.text, c.unknown))
# TODO метод, показывающий статистику побед/поражений

updater.start_polling()
updater.idle()