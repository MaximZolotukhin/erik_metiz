# Ввод неограниченного числа аргументов.
def make_pizza(*toppings):
    """Выводит описание пиццы"""
    print(f"\nПриготовили пиццу с следующими топпингами: ")
    for topping in toppings:
        print(f"- {topping}")


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')