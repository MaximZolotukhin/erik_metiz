"""
Киоск с мороженым:
киоск с мороженым — особая разновидность ресторана. Напишите класс IceCreamStand, наследующий от класса
Restaurant из упражнения 9.1 (с. 175) или упражнения 9.4 (с. 180). Подойдет любая версия класса;
просто выберите ту, которая вам больше нравится. Добавьте атрибут с именем flavors для хранения списка
сортов мороженого. Напишите метод, который выводит этот список. Создайте экземпляр IceCreamStand и
вызовите этот метод.
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


class IceCreamStand(Restaurant):
    """Киоск с мороженным"""
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def get_list_flavors(self):
        """Выводит меню мороженного"""
        print("Мороженое в ассортименте:")
        for ice_cream in self.flavors:
            print(f"\t{ice_cream}")

    def append_value_flavors(self, ice_cream):
        """Добавляет мороженное в меню"""
        self.flavors.append(ice_cream)
        return self.flavors


rest_ice_cream = IceCreamStand("Баскен робинс", "Натурального мороженого")
rest_ice_cream.append_value_flavors("Атлант")
rest_ice_cream.append_value_flavors("Бодрая корова")
rest_ice_cream.append_value_flavors("Магнат")
rest_ice_cream.append_value_flavors("Серебрянная пуля")
rest_ice_cream.append_value_flavors("Чистая линия")
rest_ice_cream.get_list_flavors()
