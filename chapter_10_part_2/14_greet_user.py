"""Выводим сохраненные данные"""
import json

filename = 'username.json'

with open(filename, encoding='UTF-8') as f:
    username = json.load(f)
    print(f"С возвращением {username}")
