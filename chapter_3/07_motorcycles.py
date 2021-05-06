# Список марок мотоциклов
motorcycles = ['Harley-Davidson', 'Suzuki', 'Kawasaki', 'Honda', 'Ducati', 'Yamaha']
print(motorcycles)

# Добавление значения в список по индексу
motorcycles[0] = 'java'
print(motorcycles)

# Удаление занчения с сохранение в переменную
moto_name = motorcycles.pop(0)
print(motorcycles)

# Добавление значения в конец списка
motorcycles.append('Harley-Davidson')
print(motorcycles)

# Удаление значения из конца списка
moto_name = motorcycles.pop()
print(motorcycles)

# Добавление значения в конец списка
motorcycles.append('Yamaha')
print(motorcycles)

# Добавление указанного значения по индексу
motorcycles.insert(1, 'BMW Motorrad')
print(motorcycles)

# Удаление указанного значения по индексу
del motorcycles[0]
print(motorcycles)

# Добавление значения в указанный индекс
motorcycles[0] = 'java'
print(motorcycles)

# Удаление значения по значению
motorcycles.remove('java')
print(motorcycles)
