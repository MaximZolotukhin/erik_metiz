"""
Три ресторана:
начните с класса из упражнения 9.1. Создайте три разных экземпляра, вызовите для каждого экземпляра
метод describe_restaurant().
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

sushi_king = Restaurant("Суши кинг", "японский")
sushi_king.describe_restaurant() # Обращаемся к методу класса
print()

spanish_rest = Restaurant("Испанский", "испанской")
spanish_rest.describe_restaurant() # Обращаемся к методу класса
print()

lai_lack = Restaurant("Лей Лак", "восточной")
lai_lack.describe_restaurant() # Обращаемся к методу класса
