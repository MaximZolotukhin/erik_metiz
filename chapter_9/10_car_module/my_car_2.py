"""Импортирование всех классов из модуля"""
# Не рекомендуется.
from car import *

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_tesla_2 = ElectricCar('tesla', 'model s3', 2020)
print(my_tesla_2.get_descriptive_name())
