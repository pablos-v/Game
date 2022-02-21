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
    if play_bot():
        update.message.reply_text('You are winner! Congrats!')
    else:
        update.message.reply_text('Bot wins. Game over.')

def play_bot():
    bank = 21
    player = randint(0, 1)
    while bank > 0:
        if player:
            bank -= move(
                f'It`s your move, player. {bank} matches left. How many will you take: ')
            player = 0
        else:
            turn = bot_logic(bank)
            bank -= turn
            update.message.reply_text(f'Bot`s move. Bot is taking {turn} matches.')
            player = 1
    return not player


def move(s):
    while True:
        try:
            num = int(input(s))
            if 1 <= num <= 4:
                return num
            else:
                update.message.reply_text('You can take only 1, 2, 3 or 4 matches!!!')
                continue
        except ValueError:
            update.message.reply_text("Something is wrong, try one more time!")


def bot_logic(s):
    if not s % 5:
        return randint(1, 4)
    else:
        return s % 5

#     update.message.reply_text(f'{x} + {y} = {x+y}')

# def pict(update: Update, context: CallbackContext):
#     msg = update.message.text
#     items = msg.split()# сплитим сообщение на /pict 1 2 3
#     a = int(items[1])
#     b = int(items[2])
#     c = int(items[3])
#     x = np.arange(a, b, c)
#     y = np.sin(x)
#     plt.plot(x, y)
#     plt.savefig('saved_figure.png') #сохраняем график в файл
#     #update.message.reply_text(f'sin {a}, {b}, {c}')
#     photo_file = open("saved_figure.png",'rb')
#     context.bot.sendPhoto(chat_id=update.message.chat_id,
#                             photo=photo_file,
#                             caption=(f'sin {a}, {b}, {c}'))
 