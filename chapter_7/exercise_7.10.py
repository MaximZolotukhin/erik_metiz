"""
Отпуск мечты:
напишите программу, которая опрашивает пользователей, где бы они хотели провести отпуск.
Включите блок кода для вывода результатов опроса.
"""
# Создаем пустой словарь
user_travel = {}
# Делаем флаг остановки
action_flag = True
while action_flag:
    user = input('Введите ваше имя: ') # Создаем переменную с именем пользователя для словарая
    user_travel[user] = input('Введите страну где вы хотите отдохнуть: ') # Записываем в словарь имя и место где хочет отдохнуть человек
    cont = input('вы желаете продолжить да/нет: ') # Если человек желает закончить вводить данные, он должен ввести слово 'нет'
    if cont == 'нет':
        action_flag = False
    else:
        continue

# Вывод результата работы цикла while
for name, places in user_travel.items():
    print(f"{name.title()} хочет отдохнуть в {places.title()}")
