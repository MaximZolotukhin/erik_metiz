"""
Город, страна:
напишите функцию, которая получает два параметра: название страны и название города.
Функция должна возвращать одну строку в формате «Город, Страна» — например, «Santiago, Chile».
Сохраните функцию в модуле с именем city_functions.py.
Создайте файл test_cities.py для тестирования только что написанной функции
(не забудьте импортировать unittest и тестируемую функцию). Напишите метод test_city_country()
для проверки того, что вызов функции с такими значениями, как 'santiago' и 'chile', дает правильную строку.
Запустите test_cities.py и убедитесь в том, что тест test_city_country() проходит успешно.
"""

# Тестирование функции
def get_formatted_name(name_country, name_city, population_size = 0):
    """Строит отфорамтированное полное имя."""
    if population_size:
        full_position = f"{name_country} {name_city} {population_size}"
    else:
        full_position = f"{name_country} {name_city}"
    return full_position.title()