# Изменение атрибутов

class Car():
    def __init__(self, manufacturer, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometr_readin = 0

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание."""
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

    def read_odometr(self):
        """Выводит пробег машины"""
        print(f"Эта машина проехала {self.odometr_readin} км.")

my_new_car = Car('audi', 'A4', '2019')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometr()

my_new_car.odometr_readin = 23
my_new_car.read_odometr()
