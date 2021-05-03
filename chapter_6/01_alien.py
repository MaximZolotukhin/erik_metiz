# Создание словаря.
alien_0 = {'color': 'green', 'points': 5}

# Обращение к значению словаря по ключу
print(alien_0['color'])
print(alien_0['points'])

# сохранинее значению словаря по ключу в новую переменную
new_points = alien_0['points']
print(f'Вы заработали {new_points} очков')

# Добавление значение в словарь
alien_0['x_position'] = 0
alien_0['y_position'] = 25
# Изменения значения словаря
alien_0['color'] = 'red'
print(alien_0)

# Создание пустого словаря и заполнения его занчениями
alien_1 = {}
alien_1['color'] = 'red'
alien_1['points'] = 10
alien_1['x_position'] = 25
alien_1['y_position'] = 25

# Удаляем значение и позицию из словаря
del alien_0['points']

print(alien_1)
print(alien_0)
