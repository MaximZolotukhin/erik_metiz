"""Наследование"""
# Изменение атрибутов с приращение заданной величены.

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

    def increment_odometr(self, miles):
        """Увеличивает покзания одометра с заданным приращением"""
        self.odometr_readin += miles


class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей."""

    def __init__(self, make, model, year):
        """инициализирует атрибуты класс-родителя."""
        super().__init__(make, model, year)


my_tesla = ElectricCar('tesla', 'model s', '2019')
print(my_tesla.get_descriptive_name())
