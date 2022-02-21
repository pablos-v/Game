# 39 Помните игру с конфетами из модуля "Математика и Информатика"?
# Создайте такую игру для игры человек против человека
#   a Добавьте игру против бота
#   b Подумайте как наделить бота "интеллектом"

#  суть игры: на столе 21 спичка, за ход можно взять от 1 до 4 спичек
# побеждает тот, кто забрал последнюю
from random import randint


def main():
    print('There are 21 matches on the table, you can take from 1 to 4 matches per turn.\n\
Last hand wins.')
    if play_bot():
        print('You are winner! Congrats!')
    else:
        print('Bot wins. Game over.')
        


def bot_logic(s):
    if not s % 5:
        return randint(1, 4)
    else:
        return s % 5


def move(s):
    while True:
        try:
            num = int(input(s))
            if 1 <= num <= 4:
                return num
            else:
                print('You can take only 1, 2, 3 or 4 matches!!!')
                continue
        except ValueError:
            print("Something is wrong, try one more time!")


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
            print(f'Bot`s move. Bot is taking {turn} matches.')
            player = 1
    return not player

