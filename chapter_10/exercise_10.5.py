"""
Опрос:
напишите цикл while, в котором программа спрашивает у пользователя, почему ему нравится программировать.
Каждый раз, когда пользователь вводит очередную причину, сохраните текст его ответа в файле.
"""
answer_users = "love_program.txt"

with open(answer_users, 'a', encoding='UTF-8') as answer_list:
    while True:
        answer_user = input("Почему Вам нравится программированть: ")
        if answer_user == 'n':
            break
        answer_list.write(f"{answer_user}\n")