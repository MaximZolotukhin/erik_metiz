"""
Гость:
напишите программу, которая запрашивает у пользователя его имя.
Введенный ответ сохраняется в файле с именем guest.txt.
"""

file_path = 'guest.txt'

with open(file_path, 'w', encoding="UTF-8") as guest_list:
    name = input('Пожалуйста представьтесь: ')
    guest_list.write(name)
