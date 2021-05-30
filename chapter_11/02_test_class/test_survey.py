"""Тестирование на правильность работы 0класса."""
import unittest
from survey import AnonymusSurvey

class TestAnonymusSurvey(unittest.TestCase):
    """Тесты для класса AnonymusSurvey"""

    def test_store_single_response(self):
        """Проверяет что один ответ сохранен правильно."""
        question = "Какой был ваш первый язык? "
        my_survey = AnonymusSurvey(question)
        my_survey.store_response("Русский")
        self.assertIn('Русский', my_survey.responses)

    def test_store_three_responses(self):
        """Проверяет, что три ответа были сохранены правильно."""
        question = "Какой был ваш первый язык? "
        my_survey = AnonymusSurvey(question)
        responses = ["Русский", "Английский", "Итальянский"]
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)

if __name__ == '__main__':
    unittest.main()
