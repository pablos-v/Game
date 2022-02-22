from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from random import randint

database = {} # will be like {ID:[Name,bank]}
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("unknown command: " + update.message.text)

def help(update: Update, context: CallbackContext):
    update.message.reply_text(f'It`s a game. There are 21 matches on the table, you can take from 1 to 4 matches per turn.\n\
Last hand wins.\n To start the game just send /run')

def user(update, context):
    if update.effective_user.id in database: # Do we know him?
        print()
    else:
        database.update({update.effective_user.id : [update.effective_user.first_name, 21]}) # TODO add params to count wins and losses
 

def run(update: Update, context: CallbackContext):
    user(update, context)
    if database[update.effective_user.id][1] <= 0: # If he played and bank is empty
            database[update.effective_user.id][1] = 21 # He will play again
        # If player continues game after pause - we remember the last bank TODO add greetings by name
            update.message.reply_text(f'Trere are {database[update.effective_user.id][1]} matches in the heap,\n send /turn and the number of matches you want to take.')
    else: # If he is new player - we remember him and add bank 21 match
        update.message.reply_text(f'Trere are {database[update.effective_user.id][1]} matches in the heap,\n send /turn and the number of matches you want to take.')


def turn(update: Update, context: CallbackContext):
    user(update, context)
    msg = update.message.text # read user`s input
    if len(msg.split())<2:
        update.message.reply_text(f'You did not enter the numbers of matches. Please entered /turn and number')
    else:
        database[update.effective_user.id][1] -= int(msg.split()[1]) # count bank after user`s move TODO check 1 <= input <= 4
        if database[update.effective_user.id][1] <= 0:
            update.message.reply_text(f'You take the last one and win the game!\n Type /run to play again.')
            # TODO count wins
            return
        update.message.reply_text(f'{database[update.effective_user.id][1]} matches left, bot`s turn.')

        bot_take = bot_logic(database[update.effective_user.id][1])
        database[update.effective_user.id][1] -= bot_take
        if database[update.effective_user.id][1] <= 0:
            update.message.reply_text(f'Bot has taken the last one and wins the game... You loose.\n Type /run to play again!')
            # TODO count losses
            return
        update.message.reply_text(f'Bot takes {bot_take} matches, {database[update.effective_user.id][1]} matches left.')


def bot_logic(s):
    if not s % 5:
        return randint(1, 4)
    else:
        return s % 5

 
 
