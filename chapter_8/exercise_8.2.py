"""
Любимая книга:
напишите функцию favorit_book(), которая получает один параметр title. Функция должна выводить сообщение вида
"One of my favorite books is Alice in Wonderland". Вызовите функцию и убедитесь в том, что название книги
 правильно передается как аргумент при вызове функции.
"""

def favorit_book(title):
    """
    Функция выводит название книги
    :param title: получает аргумент с название любимой книги.
    :return:
    """
    print(f"Моя любимая книга {title}")

favorit_book("Ведьмак")
