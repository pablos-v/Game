from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import commands as c



updater = Updater('5110228065:AAGeoqKoZEpzIhU5GD_b76QLXmuf01uwp9I')
print("Server started")
# TODO check the input and show help for every input without commands
updater.dispatcher.add_handler(CommandHandler('help', c.help))
updater.dispatcher.add_handler(CommandHandler('run', c.run))
updater.dispatcher.add_handler(CommandHandler('turn', c.turn))
# TODO make method showing user`s win/loss statistics

updater.start_polling()
updater.idle()