"""Сохраняет и стчтывает данные из файла"""
import json

# Программа загружает имя пользователя, если оно было сохранено ранее.
# В противном случае она запрашивает имя пользователя и сохраняет его.

filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("Как ваше имя: ")
    with open(filename, 'w', encoding='UTF-8') as f:
        json.dump(username, f)
        print(f'\nМы вспомним ваше имя когда вы вернетесь {username}!')
else:
    print(f"С возвращением {username}")
