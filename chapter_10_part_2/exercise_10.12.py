"""
Сохраненное любимое число:
объедините две программы из упражнения 10.11 в один файл. Если число уже сохранено,
сообщите его пользователю, а если нет — запросите любимое число пользователя и
сохраните в файле. Выполните программу дважды, чтобы убедиться в том, что она работает.
"""
import json

filepath = "love_number.txt"

try:
    with open(filepath, 'r') as f:
        love_nimber = json.load(f)
        print(love_nimber)
except FileNotFoundError:
    love_number = input("Введите ваше любимое число: ")
    with open(filepath, 'w') as f:
        json.dump(love_number, f)







