# Создание модулей содержащих классы
"""Класс для представления автомобиля"""
class Car():
    """Простая модель автомобиля"""
    def __init__(self, manufacturer, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometr_readin = 0

    def get_descriptive_name(self):
        """
        Инициализирует атрибуты класс-родителя.
        Затем иницилазирует атрибуты, специфически для электромобиля.
        """
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

class Battery():
    """Простая модель аккумулятора электромобиля."""
    def __init__(self, battery_size=75):
        """Инициализирует атрубуты аккумулятора"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print(f"В этой машине установлен аккумулятор мощностью {self.battery_size}-kWh.")

    def get_range(self):
        """Выводит приблезительный запас хода для аккумулятора."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"Эта машина может проехать {range} на {self.battery_size}% заряда аккумулятора")


class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей."""

    def __init__(self, make, model, year):
        """инициализирует атрибуты класс-родителя."""
        super().__init__(make, model, year)
        self.battery = Battery()
