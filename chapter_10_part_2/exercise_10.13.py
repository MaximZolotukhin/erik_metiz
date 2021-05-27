"""
Проверка пользователя:
последняя версия remember_me.py предполагает, что пользователь либо уже ввел свое имя,
либо программа выполняется впервые. Ее нужно изменить на тот случай, если текущий
пользователь не является тем человеком, который последним использовал программу.
Прежде чем выводить приветствие в greet_user(), спросите, правильно ли определено
имя пользователя. Если ответ будет отрицательным, вызовите get_new_username()
для получения правильного имени пользователя.
"""

import json

# Программа загружает имя пользователя, если оно было сохранено ранее.
# В противном случае она запрашивает имя пользователя и сохраняет его.

def get_sorted_username():
    """Получить хранимое имя пользователя, если оно существует"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Запрашивает новое имя пользователя"""
    username = input("Как ваше имя: ")
    filename = 'username.json'
    with open(filename, 'w', encoding='UTF-8') as f:
        json.dump(username, f)
    return username

def getter_user():
    """Приветсвует пользователя по имени"""
    name = input("Введите свое имя: ")
    username = get_sorted_username()
    if username == name:
        print(f"С возвращением {username}")
    else:
        username = get_new_username()
        print(f'Мы вспомним ваше имя когда вы вернетесь {username}!')

getter_user()
