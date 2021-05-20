"""
Лотерея:
создайте список или кортеж, содержащий серию из 10 чисел и 5 букв.
Случайным образом выберите 4 числа или буквы из списка.
Выведите сообщение о том, что билет, содержащий эту комбинацию из
четырех цифр или букв, является выигрышным.
"""
from random import choice

tuple_loto = (1, 2, 5, 7, 'A', 3, 'E', 4, 'B', 'C', 6, 8, 'D', 9, 0)


def loto(numb_or_letter):
    """Функция выбирает из кортежа данные и сохраняет 4 символа в список"""
    flag_stop = True
    winning_values = []
    count = 1
    while flag_stop:
        value = choice(numb_or_letter)
        winning_values.append(value)
        if count == 4:
            flag_stop = False
        count += 1
    return winning_values

values = loto(tuple_loto)
print(f"Выгрышные номера {values}")
