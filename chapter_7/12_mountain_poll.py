# Программа сохраняем полученные данные в словарь
responses = {} # Создаем пустой словарь.

# Установка флага продолжения опроса.
polling_active = True

while polling_active:
    # Запрос имени и ответа пользователя.
    name = input("\nЗапшите ваше имя: ")
    response = input("\nНа какоую гору вы хотели бы подняться? ")

    # Ответ
    responses[name] = response

    # Проверка продолжения опроса.
    repeat = input("Хотели бы вы дать ответить другому челвоеку? (да/нет) ")
    if repeat == 'нет':
        polling_active = False
# Опрос завершен, вывести результат
for name, response in responses.items():
    print(f"{name.title()} хотел подняться на {response.title()}")
