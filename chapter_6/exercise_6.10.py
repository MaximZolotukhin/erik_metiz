"""
Любимые числа:
Измените программу из упражнения 6.2 (с 114), чтобы для каждого
челвоека можно было хранить более одного любимого числа. Выведите имя каждого человека
в списке и его любмимые числа.
"""
# Словарь с вложенным списком.
love_number = {
    'Ольга': [7, 46, 77],
    'Максим': [6, 7, 3, 666, 777],
    'Василий': [1, 12, 56],
    'Наталья': [1, 6, 4],
    'Олег': [9, 56, 81],
}
# Перебор значений.
for name, number in love_number.items():
    print(f"{name.title()} любимые числа: ")
    for num in number:
        print(f"{num},", end=" ")
    print('\n')
