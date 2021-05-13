def make_pizza(size, *toppings):
    """Выводит описание пиццы"""
    print(f"\nПриготовили пиццу размером {size} дюйомов, с следующими топпингами: ")
    for topping in toppings:
        print(f"- {topping}")
