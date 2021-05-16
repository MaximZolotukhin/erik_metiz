# Изменение атрибутов с помощью метода

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

    def update_odometr(self, mileage):
        """
        Устанавливает заданное значение на одометре
        При попытки обратной подкрутки значение отклоняется.
        """
        if mileage >= self.odometr_readin:
            self.odometr_readin = mileage
        else:
            print(f"Вы не можете скрутить киллометры.")

my_new_car = Car('audi', 'A4', '2019')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometr()

my_new_car.update_odometr(51)
my_new_car.read_odometr()
