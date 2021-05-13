"""
Сообщения:
создайте список с серией коротких сообщений. Передайте список функций show_messages(),
которая выводит текст каждого сообщения в списке.
"""

short_messages = ['Привет', 'Пока', 'Как дела?', 'Куды прешь']

def show_messages(short_messages):
    for message in short_messages:
        print(message)


show_messages(short_messages)
