from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import commands as c



updater = Updater('5293815590:AAES4pa-TLVjgbu8zNp9fn6f19uboSJ1Lek')
print("Server started")
# TODO check the input and show help for every input without commands
updater.dispatcher.add_handler(CommandHandler('help', c.help))
updater.dispatcher.add_handler(CommandHandler('run', c.run))
updater.dispatcher.add_handler(CommandHandler('turn', c.turn))
# TODO make method showing user`s win/loss statistics

updater.start_polling()
updater.idle()