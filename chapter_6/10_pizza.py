# Сохраниение списка в словаре
# Сохранение информации о заказанной пицце.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Описание заказа.
print(f"Вы заказали {pizza['crust']} - crust pizza, с добавлением топингов:")

for topping in pizza['toppings']:
    print("\t" + topping)
