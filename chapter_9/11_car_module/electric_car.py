"""Второй модуль для элкетромобилей"""
from car import Car

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
