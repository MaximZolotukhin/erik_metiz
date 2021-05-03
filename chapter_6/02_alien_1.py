alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Оригинальная позиция: {alien_0['x_position']}")

# Пришелец перемещается вправо.
# Вычисляем величину смещения на основании текущей скорости.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # Пришелец двигается быстро
    x_increment = 3

# Новая позиция равна сумму старой позиции и приращения.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"Новая произция: {alien_0['x_position']}")
