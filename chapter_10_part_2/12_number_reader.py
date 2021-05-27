"""Чтение данных из файла"""
import json

filename = 'numbers.json'

with open(filename, 'r', encoding='UTF-8') as f:
    numbers = json.load(f)

print(numbers)
