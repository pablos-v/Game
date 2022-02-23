from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import commands as c



updater = Updater('5137029532:AAGy_rqWXURCQEsYj2zqfp1UUwUjlOijNEM')
print("Server started")
# TODO check the input and show help for every input without commands

updater.dispatcher.add_handler(CommandHandler('help', c.help))
updater.dispatcher.add_handler(CommandHandler('run', c.run))
updater.dispatcher.add_handler(CommandHandler('turn', c.turn))
updater.dispatcher.add_handler(MessageHandler(Filters.command, c.unknown))
# TODO make method showing user`s win/loss statistics

updater.start_polling()
updater.idle()