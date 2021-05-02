# Если список топпингов постоянный нужно использовать кортеж
available_toppings = ('mushrooms', 'olives', 'green peppers', 'pepperoni', 'extra cheese', 'pipneapple')

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'В пиццу добавлен {requested_topping}')
    else:
        print(f'Извините у нас нет {requested_topping}')

print("\nЗакончить приготовление пиццы\n")