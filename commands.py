from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from random import randint

def hello(update: Update, context: CallbackContext):
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def help(update: Update, context: CallbackContext):
    update.message.reply_text(f'hello, help, run')

def run(update: Update, context: CallbackContext):
    update.message.reply_text('There are 21 matches on the table, you can take from 1 to 4 matches per turn.\n\
Last hand wins.')
    if play_bot(update, context):
        update.message.reply_text('You are winner! Congrats!')
    else:
        update.message.reply_text('Bot wins. Game over.')

def play_bot(update: Update, context: CallbackContext):
    bank = 21
   # player = randint(0, 1)
    #while bank > 0:
       
    turn = bot_logic(bank)
    bank -= turn #тг, что прислал пользователь Если равно нулю, пользователь победил
    if bank ==0:
        update.message.reply_text(f'Bot`s move. Bot is taking {turn} matches.')
    else:
        # -= ход бота
    if bank == 0:
        # сообщение бот победил
    
            
def bot_logic(s):
    if not s % 5:
        return randint(1, 4)
    else:
        return s % 5

