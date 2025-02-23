import commands as c
from random import randint
from telegram import Update
from telegram.ext import CallbackContext
import log
import time
import db_sqlite as db

bank = 'bank'

# ход игрока
def turn(update: Update, context: CallbackContext):
    c.user(update, context)
    msg = update.message.text
    if input_check(msg): #  проверка ввода
        db.edit_bank(update.effective_user.id, int(msg))
        if db.ask(bank, update.effective_user.id) <= 0: # проверка на победу
            update.message.reply_text('Вы берёте последнюю спичку и побеждаете в игре!\n\
Команда /stats покажет вашу статистику игр.')
            db.winloss(1, update.effective_user.id) # счётчик побед
            log.write(update.effective_user.id, update.effective_user.first_name, 1)
            time.sleep(1)
            update.message.reply_text('Я снова насыпал 21 спичку на стол и прошу реванш!\n\
Сколько спичек возьмёте?')
            return
        update.message.reply_text(f'Теперь на столе {s(db.ask(bank, update.effective_user.id))}, \
хожу я.')
        bot_turn(update, context)
    else:
        unknown(update, context)


# ход бота
def bot_turn(update: Update, context: CallbackContext):
    bot_take = bot_logic(db.ask(bank, update.effective_user.id))
    db.edit_bank(update.effective_user.id, int(bot_take))
    update.message.reply_text(f'Я беру {bot_take}, остаётся {s(db.ask(bank, update.effective_user.id))}.')   
    if db.ask(bank, update.effective_user.id) <= 0: # проверка на проигрыш
        update.message.reply_text(f'Вы проиграли, я забрал последнюю спичку...\n\
Команда /stats покажет вашу статистику игр.')
        db.winloss(0, update.effective_user.id) # счётчик поражений
        log.write(update.effective_user.id, update.effective_user.first_name, 0)
        time.sleep(1)
        update.message.reply_text('Я ещё не устал и могу сыграть снова! На столе опять 21 спичка.\n\
Сколько возьмёте?')
    update.message.reply_text('Ваш ход.')


# логика бота
def bot_logic(s):
    if not s % 5:
        return randint(1, 4)
    else:
        if randint(1, 10) > 4: # вероятность ошибки 40%
            return s % 5
        else:
            return randint(1, 4)


# проверка ввода
def input_check(msg):
    try:
        return 1 <= int(msg) <= 4
    except:
        return 0


# правильно склоняем слово "спичка"
def s(n):
    if n % 10 == 1 and n != 11:
        return f'{n} спичка'
    elif n % 10 in [2, 3, 4] and not n in [12, 13, 14]:
        return f'{n} спички'
    else:
        return f'{n} спичек'


# сообщение о неизвестной команде
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(f'Я вот прям не знаю как на это ваше "{update.message.text}" \
реагировать... Расслабьтесь, почитайте /help')