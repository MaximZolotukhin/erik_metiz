# Изменение атрибутов

class Car():
    def __init__(self, manufacturer, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание."""
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()


my_new_car = Car('audi', 'A4', '2019')
print(my_new_car.get_descriptive_name())
