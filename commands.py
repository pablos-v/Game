from telegram import Update
from telegram.ext import CallbackContext
import game_logics as g

database = {} # БД вида {ID:[Имя, банк, побед, поражений]}
bank = 1 # номер элемента списка в БД
wins = 2
loss = 3


# вывод статистики игрока
def stats(update: Update, context: CallbackContext):
    user(update, context)
    update.message.reply_text(f'{update.effective_user.first_name}, вы одержали\nпобед: \
{database[update.effective_user.id][wins]}\nпоражений: {database[update.effective_user.id][loss]}\
\n\nХотите сыграть ещё?\nНа столе {g.s(database[update.effective_user.id][bank])}, сколько берёте?')


def help(update: Update, context: CallbackContext):
    user(update, context)
    update.message.reply_text(f'Приветствую {update.effective_user.first_name}, это простая игра.\n\
На столе лежит {g.s(database[update.effective_user.id][bank])}. Вы можете брать от 1 до 4 спичек за ход.\n\
Победит тот, кто заберёт последнюю. Команда /cheat покажет подсказку.\nСколько спичек возьмёте?\n')


# подсказка
def cheat(update: Update, context: CallbackContext):
    user(update, context)
    if database[update.effective_user.id][bank] % 5:
        update.message.reply_text(f'Так и быть, подскажу. Сейчас лучше всего взять {database[update.effective_user.id][bank] % 5}')
    else:
        update.message.reply_text(f'Иногда лучше просто плыть по течению, сделайте ход.')
    return


# проверка и добавление пользователя в БД
def user(update: Update, context: CallbackContext):
    if update.effective_user.id not in database:
        database.update({update.effective_user.id:[update.effective_user.first_name, 21, 0, 0]})

