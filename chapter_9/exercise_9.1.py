"""
Ресторан:
создайте класс с именем Restaurant. Метод __init__() класса Restaurant должен содержать два атрибута:
restaurant_name и cuisine_type. Создайте метод describe_restaurant(), который выводит два атрибута,
и метод open_restaurant(), который выводит сообщение о том, что ресторан открыт. Создайте на основе своего
класса экземпляр с именем restaurant. Выведите два атрибута по отдельности, затем вызовите оба метода.
"""


class Restaurant():
    """Класс с описанием ресторана"""

    def __init__(self, restaurant_name, cuisine_type):
        """Создаем конструктор с значениями которые можно будет передать"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def open_restaurant(self):
        """Метод выводит возвращает слово открыт"""
        open = "открыт!"
        return open

    def describe_restaurant(self):
        """Метод выдает сообщения со всеми элементами класса"""
        print(f"Ресторан {self.restaurant_name.title()} с {self.cuisine_type} кухней {self.open_restaurant()}")


# Создаем экземпляр класса
sushi_king = Restaurant("Суши кинг", "японский")
sushi_king.describe_restaurant() # Обращаемся к методу класса
print()

spanish_rest = Restaurant("Испанский", "сырный")
print(spanish_rest.restaurant_name) # Обращаеся с полям класса
print(spanish_rest.cuisine_type) # Обращаеся с полям класса
spanish_rest.describe_restaurant()
print(f"{spanish_rest.open_restaurant()}")
