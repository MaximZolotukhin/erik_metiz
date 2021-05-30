"""Тестирование на правильность работы 0класса."""
import unittest
from survey import AnonymusSurvey

class TestAnonymusSurvey(unittest.TestCase):
    """Тесты для класса AnonymusSurvey"""

    def setUp(self):
        """Создание опроса и набора ответов для всех тестовых методов."""
        question = "Какой был ваш первый язык? "
        self.my_survey = AnonymusSurvey(question)
        self.responses = ["Русский", "Английский", "Итальянский"]

    def test_store_single_response(self):
        """Проверяет что один ответ сохранен правильно."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Проверяет, что три ответа были сохранены правильно."""
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()
