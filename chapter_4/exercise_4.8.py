"""
Кубы:
результат возведения числа в третью степень называется кубом.
Например, куб 2 записывается в языке Python в виде 2**3.
Создайте список первых 10 кубов (то есть кубов всех целых чисел от 1 до 10)
и выведите значения всех кубов в цикле for.
"""
#Варинат 1
list_qub = []

for num in range(1, 10):
    num_qub = num**3
    list_qub.append(num_qub)

print(list_qub)

#Варинат 2
list_qub_1 = []

for num in range(1, 10):
    list_qub_1.append(num**3)

print(list_qub_1)
