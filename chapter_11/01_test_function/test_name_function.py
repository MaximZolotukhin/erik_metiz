import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Тесты для 'name_function.py'"""

    def test_first_last_name(self):
        """Имена вида 'Jains Joplin' работают правильно"""
        formatted_name = get_formatted_name('Jains', 'Joplin')
        self.assertEqual(formatted_name, 'Jains Joplin')

    def test_first_last_name(self):
        """Имена вида 'Александр Пушкин Сергеевич' работают правильно"""
        formatted_name = get_formatted_name('Александр', 'Пушкин', 'Сергеевич')
        self.assertEqual(formatted_name, 'Александр Сергеевич Пушкин')

if __name__ == '__main__':
    unittest.main()

