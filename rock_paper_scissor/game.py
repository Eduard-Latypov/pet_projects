import random  # импортируем модуль рандом

# инициализируем переменные
choices = {'r': 'Камень', 'p': 'Бумага', 's': 'Ножницы'}
cPoints = 0
pPoints = 0


def player():
    '''Функция для получения выбора игрока'''

    global choices
    print('Сделай выбор!')
    symbol = input("Камень(r), Бумага(p), или Ножницы(s). ").lower()

    if symbol not in choices:
        print("Проверьте правильность ввода и повторите попытку")
        return player()  # используем рекурсию, пока не получим валидные данные
    else:
        return symbol  # если данные валидные, то возвращем их


def computer():
    '''Функция для выбора компьютера'''

    return random.choice(list(choices.keys()))


def game():
    '''Один раунд игры'''

    global cPoints, pPoints, choices
    pChoice = player()
    cChoice = computer()
    print("Выбор компьютера: ", choices[cChoice])
    print("Твой выбор: ", choices[pChoice])
    if pChoice == cChoice:
        print("Ничья! ")
    elif (pChoice == "r" and cChoice == "s") or (pChoice == "s" and cChoice == "p") or (pChoice == "p" and cChoice == "r"):

        print("Ты выиграл! ")
        pPoints += 1
    else:
        print("Оуу. Я выиграл. ")
        cPoints += 1
    print()


print("Добро пожаловать в игру камень, ножницы, бумага!!!")
while True:
    for i in range(5):
        game()
    print("Хорошая работа!\nТвои показатели: ", pPoints, "\nМои показатели: ",
          cPoints)
    print()
    again = int(
        input("1 - Продолжить\n2 - Рестарт\n3 - Выход\n"))
    if again == 1:
        continue
    elif again == 2:
        pPoints = 0
        cPoints = 0
        continue
    else:
        break

print("Всего доброго!")
