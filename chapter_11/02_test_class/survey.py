"""Тестирование класса"""

class AnonymusSurvey():
    """Сбор анонимыных ответов на опросы."""

    def __init__(self, question):
        """Сохраняет вопрос и готовится к сохранению ответов."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Выводит вопрос"""
        print(self.question)

    def store_response(self, new_response):
        """Сохраняет один ответ на опрос"""
        self.responses.append(new_response)

    def show_result(self):
        """Выводит все полученные ответы."""
        print("Отображаем результат: ")
        for response in self.responses:
            print(f"- {response}")
