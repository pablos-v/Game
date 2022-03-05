from email import message
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from random import randint


database = {} # БД вида {ID:[Имя, банк, побед, поражений]}
bank = 1 # номер элемента списка в БД
wins = 2
loss = 3


# сообщение о неизвестной команде
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(f'Я вот прям не знаю как на это ваше "{update.message.text}" \
реагировать... Расслабьтесь, почитайте /help')


# вывод статистики игрока
def stats(update: Update, context: CallbackContext):
    user(update, context)
    update.message.reply_text(f'{update.effective_user.first_name}, вы одержали\nпобед: \
{database[update.effective_user.id][wins]}\nпоражений: {database[update.effective_user.id][loss]}\
\n\nХотите сыграть ещё? На столе {s(database[update.effective_user.id][bank])}, сколько берёте?')


def help(update: Update, context: CallbackContext):
    user(update, context)
    update.message.reply_text(f'Приветствую {update.effective_user.first_name}, это простая игра. \
На столе лежит {s(database[update.effective_user.id][bank])}. Вы можете брать от \
1 до 4 спичек за ход.\nПобедит тот, кто заберёт последнюю.\nСколько штук возьмёте?')


# проверка и добавление пользователя в БД
def user(update: Update, context: CallbackContext):
    if update.effective_user.id not in database:
        database.update({update.effective_user.id:[update.effective_user.first_name, 21, 0, 0]})


# ход игрока
def turn(update: Update, context: CallbackContext):
    user(update, context)
    msg = update.message.text
    if input_check(msg): #  проверка ввода
        database[update.effective_user.id][bank] -= int(msg)
        if database[update.effective_user.id][bank] <= 0: # проверка на победу
            update.message.reply_text('Вы берёте последнюю спичку и побеждаете в игре!\n\
Команда /stats покажет вашу статистику игр.')
            database[update.effective_user.id][wins] += 1 # счётчик побед
            database[update.effective_user.id][bank] = 21
            update.message.reply_text('Я снова насыпал 21 спичку на стол и прошу реванш!\n\
Сколько спичек возьмёте?')
            return
        update.message.reply_text(f'Теперь на столе {s(database[update.effective_user.id][bank])}, \
ходит бот.')
        bot_turn(update, context)
    else:
        unknown(update, context)
        

# ход бота
def bot_turn(update: Update, context: CallbackContext):
    bot_take = bot_logic(database[update.effective_user.id][bank])
    database[update.effective_user.id][bank] -= bot_take
    update.message.reply_text(f'Бот забирает {bot_take}, остаётся {s(database[update.effective_user.id][bank])}.')   
    if database[update.effective_user.id][bank] <= 0: # проверка на проигрыш
        update.message.reply_text(f'Вы проиграли, бот забрал последнюю спичку...\n\
Команда /stats покажет вашу статистику игр.')
        database[update.effective_user.id][loss] += 1 # счётчик поражений
        database[update.effective_user.id][bank] = 21
        update.message.reply_text('Я ещё не устал и могу сыграть снова! На столе опять 21 спичка.\n\
Сколько возьмёте?')
        return
    update.message.reply_text('Ваш ход.')


# логика бота
def bot_logic(s):
    if not s % 5:
        return randint(1, 4)
    else:
        if randint(1, 10) > 3: # вероятность ошибки 30%
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