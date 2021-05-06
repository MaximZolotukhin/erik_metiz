# Создание пустого списка для хранения пришельцев.
aliens = []

# Создание 30 зеленых пришельцев
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Изменения значений пришельцев
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

# Вывод первых 5 пришельцев:
for alien in aliens[:5]:
    print(alien)
print("...")

# Вывод количества созданных пришельцев
print(f"Всего созданной пришельцев: {len(aliens)}")
