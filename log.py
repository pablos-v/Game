import datetime

# логирование в формате ID, Имя, Время и Дата, 0/1 - поражение/победа
def write(ID, who, x):
    with open('Game/log.csv', 'a', encoding='UTF8') as file:
        file.write(f'{ID}, {who}, {datetime.datetime.now()}, {x}\n')
