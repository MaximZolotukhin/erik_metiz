"""Класс Restaurant в отдельном модуле"""
class Restaurant():
    """Класс с описанием ресторана"""

    def __init__(self, restaurant_name, cuisine_type):
        """Создаем конструктор с значениями которые можно будет передать"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def open_restaurant(self):
        """Метод выводит возвращает слово открыт"""
        open = "открыт!"
        return open

    def describe_restaurant(self):
        """Метод выдает сообщения со всеми элементами класса"""
        print(f"Ресторан {self.restaurant_name.title()} с {self.cuisine_type} кухней {self.open_restaurant()}")

    def set_number_served(self, people_served):
        """Считает количество обслуженных людей"""
        self.number_served = people_served

    def increment_number_served(self):
        """При каждом вызове увеличивает количество обслуженных человек на 1"""
        self.number_served += 1
