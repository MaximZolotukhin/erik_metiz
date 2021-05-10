"""
Цель програмы показать работу оператора continue
"""
# Программа выводит нечетные числа.
curren_number = 0
while curren_number < 10:
    curren_number += 1
    if curren_number % 2 == 0:
        continue # При выполнение этого оператора цикл переходи в начало игнорируя все что ниже оператора continue

    print(curren_number)
