"""
Посетители:
начните с программы из упражнения 9.1 (с. 175). Добавьте атрибут number_served со значением по умолчанию 0;
он представляет количество обслуженных посетителей. Создайте экземпляр с именем restaurant.
Выведите значение number_served, потом измените и выведите снова.
Добавьте метод с именем set_number_served(), позволяющий задать количество обслуженных посетителей.
Вызовите метод с новым числом, снова выведите значение.
Добавьте метод с именем increment_number_served(), который увеличивает количество обслуженных
посетителей на заданную величину. Вызовите этот метод с любым числом, которое могло бы представлять
количество обслуженных клиентов, — скажем, за один день.
"""


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

# Создаем экземпляр класса
restaurant = Restaurant("Суши кинг", "японский")
print(restaurant.number_served)
restaurant.number_served = 2
print(restaurant.number_served)

restaurant.set_number_served(3)
print(restaurant.number_served)

restaurant.increment_number_served()
print(restaurant.number_served)
