from telegram import Update
from telegram.ext import CallbackContext
import game_logics as g
import db_sqlite as db

bank = 'bank'
wins = 'wins'
loss = 'loss'


# вывод статистики игрока
def stats(update: Update, context: CallbackContext):
    user(update, context)
    update.message.reply_text(f'{update.effective_user.first_name}, вы одержали\nпобед: \
{db.ask(wins, update.effective_user.id)}\nпоражений: {db.ask(loss, update.effective_user.id)}\
\n\nХотите сыграть ещё?\nНа столе {g.s(db.ask(bank, update.effective_user.id))}, сколько берёте?')


def help(update: Update, context: CallbackContext):
    user(update, context)
    update.message.reply_text(f'Приветствую {update.effective_user.first_name}, это простая игра.\n\
На столе лежит {g.s(db.ask(bank, update.effective_user.id))}. Вы можете брать от 1 до 4 спичек за ход.\n\
Победит тот, кто заберёт последнюю. Команда /cheat покажет подсказку.\nСколько спичек возьмёте?\n')


# подсказка
def cheat(update: Update, context: CallbackContext):
    user(update, context)
    q = db.ask(bank, update.effective_user.id) % 5
    if q:
        update.message.reply_text(f'Так и быть, подскажу. Сейчас лучше всего взять {q}')
    else:
        update.message.reply_text(f'Иногда лучше просто плыть по течению, сделайте ход.')
    return # TODO удалить?


# проверка и добавление пользователя в БД
def user(update: Update, context: CallbackContext):
    if update.effective_user.id not in db.idlist():
        db.adduser((update.effective_user.id, update.effective_user.first_name, 21, 0, 0))

