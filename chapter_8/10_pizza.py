# Ввод неограниченного числа аргументов.
def make_pizza(*toppings):
    """Вывод списка заказанных топпингов"""
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
