"""
Создайте файл test_cities.py для тестирования только что написанной функции
(не забудьте импортировать unittest и тестируемую функцию). Напишите метод test_city_country()
для проверки того, что вызов функции с такими значениями, как 'santiago' и 'chile', дает правильную строку.
Запустите test_cities.py и убедитесь в том, что тест test_city_country() проходит успешно.
"""
import unittest
from city_functions import get_formatted_name

class TestCities(unittest.TestCase):
    """Тестируем функцию city_function"""
    def test_city_country(self):
        test_case = get_formatted_name('Россия', 'Курск')
        self.assertEqual(test_case, 'Россия Курск')
