from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import commands as c



updater = Updater('5110228065:AAGeoqKoZEpzIhU5GD_b76QLXmuf01uwp9I')
print("Server starts")
updater.dispatcher.add_handler(CommandHandler('hello', c.hello))
updater.dispatcher.add_handler(CommandHandler('help', c.help))
updater.dispatcher.add_handler(CommandHandler('run', c.run))
updater.dispatcher.add_handler(CommandHandler('play', c.play_bot))

updater.start_polling()
updater.idle()