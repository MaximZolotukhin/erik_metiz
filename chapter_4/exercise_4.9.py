"""
Генератор кубов:
используйте конструкцию генератора списка для создания списка первых 10 кубов.
"""
list_qub = [number**3 for number in range(1, 10)]

for num in list_qub:
    print(num)