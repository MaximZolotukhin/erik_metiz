"""Программа опроса"""
from survey import AnonymusSurvey

# Определение вопроса с созданием экземпляра класс AnonymusSurvey
question = "Какой был ваш первый язык "
my_survey = AnonymusSurvey(question)

# Вывод вопроса и сохранение ответов.
my_survey.show_question()
print("Нажмите 'q' чтобы выйти.\n")
while True:
    respopnse = input("Язык: ")
    if respopnse == 'q':
        break

    my_survey.store_response(respopnse)

# Вывод результатов опроса.
print("\nСпасибо всем кто участвовал в опросе!")
my_survey.show_result()