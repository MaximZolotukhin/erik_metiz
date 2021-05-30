"""
Напишите тестовый сценарий для Employee. Напишите два тестовых метода, test_give_default_raise() и
test_give_custom_raise(). Используйте метод setUp(), чтобы вам не приходилось заново создавать экземпляр
Employee в каждом тестовом метода. Запустите свой тестовый сценарий и убедитесь в том, что оба теста прошли успешно.
"""
import unittest
from worker import Employee

class TestEmployee(unittest.TestCase):
    """Тестирование класса Employee"""

    def setUp(self) -> None:
        self.worker = Employee('Максим', 'Золотухин', 40500)

    def test_employee(self):
        self.assertEqual(self.worker.employee(), 'Максим Золотухин: оклад 40500')


if __name__ == "__main__":
    unittest.main()
