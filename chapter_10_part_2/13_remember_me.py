"""Сохранение и чтене данных, сгенерировынных пользователем"""
import json

username = input("Как ваше имя: ")

filename = 'username.json'
with open(filename, 'w', encoding='UTF-8') as f:
    json.dump(username, f)
    print(f'Мы вспомним ваше имя когда вы вернетесь {username}!')
