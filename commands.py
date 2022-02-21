from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from random import randint

database = {}


def help(update: Update, context: CallbackContext):
    update.message.reply_text(f'It`s a game. There are 21 matches on the table, you can take from 1 to 4 matches per turn.\n\
Last hand wins.\n To start the game just send /run')


def run(update: Update, context: CallbackContext):
    if update.effective_user.id in database:
        if database[update.effective_user.id][1] <= 0:
            database[update.effective_user.id][1] = 21
        update.message.reply_text(f'Trere are {database[update.effective_user.id][1]} matches in the heap,\n send /turn and the number of matches you want to take.')
    else:
        database.update({update.effective_user.id : [update.effective_user.first_name, 21]})
        update.message.reply_text(f'Trere are {database[update.effective_user.id][1]} matches in the heap,\n send /turn and the number of matches you want to take.')


def turn(update: Update, context: CallbackContext):
    msg = update.message.text
    database[update.effective_user.id][1] -= int(msg.split()[1])
    if database[update.effective_user.id][1] <= 0:
        update.message.reply_text(f'You take the last one and win the game!\n Type /run to play again.')
        return
    update.message.reply_text(f'{database[update.effective_user.id][1]} matches left, bot`s turn.')
    bot_take = bot_logic(database[update.effective_user.id][1])
    database[update.effective_user.id][1] -= bot_take
    if database[update.effective_user.id][1] <= 0:
        update.message.reply_text(f'Bot has taken the last one and wins the game... You loose.\n Type /run to play again!')
        return
    update.message.reply_text(f'Bot takes {bot_take} matches, {database[update.effective_user.id][1]} matches left.')


def bot_logic(s):
    if not s % 5:
        return randint(1, 4)
    else:
        return s % 5

 