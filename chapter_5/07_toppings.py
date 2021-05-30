"""Проверка нескольких условий"""
# ---------------- Пицца вариант 3 ----------------------
print('Пицца вариант 3')
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f'В пиццу добавлен {requested_topping}')
    print("Закончить приготовление пиццы")
else:
    print("\nВы желаете пиццу без добавок\n")


# ---------------- Пицца вариант 1 ----------------------
print('Пицца вариант 1')

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Добавить mushrooms")

if 'pepperoni' in requested_toppings:
    print("Добавить pepperoni")

if 'extra cheese' in requested_toppings:
    print("Добавить extra cheese"
          "")

print("\nЗакончить приготовление пиццы\n")

# ---------------- Пицца вариант 2 ----------------------
print('Пицца вариант 2')
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print(f'Извините у нас закончлся {requested_topping}')
    else:
        print(f'В пиццу добавлен {requested_topping}')

print("\nЗакончить приготовление пиццы\n")



