"""Создание раздлельных модулей Электромобиле и обынчх атомобилей"""
from car import Car
from electric_car import ElectricCar, Battery
from electric_car import ElectricCar as EC # Импорт модуля с сохранением его в песводоним

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_tesla_2 = ElectricCar('tesla', 'model s3', 2020)
print(my_tesla_2.get_descriptive_name())

my_tesla = EC('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())