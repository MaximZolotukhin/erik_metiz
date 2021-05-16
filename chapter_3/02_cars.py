"""Виды сортировок"""
# Сортировка по алфавиту
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# Сортировка по алфавиту в обратном порядке
cars.sort(reverse=True)
print(cars)

print('*' * 33)

# Временная сортировка списка
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('Оригинальный список cars: ')
print(cars)

print('Отсортированный список cars: ')
print(sorted(cars))

print('Снова оригинальный список cars: ')
print(cars)

print('*' * 33)

print(len(cars))
