"""
Названия городов:
напишите функцию city_country(), которая получает название города и страну.
Функция должна возвращать строку в формате "Santiago, Chile". Вызовите
свою функцию по карйне мере для трех пар "город - страна" и выведите
возвращенное значение.
"""
def city_country(city, country):
    return f"{city} - {country}"

print(city_country("Курск", "Россия"))
cityContry = city_country("Токио", "Япония")
print(cityContry)
cityContry = city_country("Париж", "Франция")
print(cityContry)
