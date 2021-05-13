# Ввод позиционного аргумента и произвольного набора.
# произвольный набор аргументов должен находится после всех аргументов
def make_pizza(size, *toppings):
    """Выводит описание пиццы"""
    print(f"\nПриготовили пиццу размером {size} дюйомов, с следующими топпингами: ")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')