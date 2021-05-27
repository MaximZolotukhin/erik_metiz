"""Простой пример"""
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw': #Если выпадает BMW тогда делаем буквы большими.
        print(car.upper())
    else:
        print(car.title())
