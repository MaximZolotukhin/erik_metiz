"""
Футболка:
напишите функцию make_shirt(), которая получает размер футболки и текст, который должен быть напечатан на
ней. Функция должна выводить сообещение с размером и текстом.
Вызовите функцию с использванием позиционных аргументов. Вызовите функцию во второй раз с использованием именованных
аргументов.
"""

def make_shirt(size, text):
    """
    Функция выводит что сделал пользователь
    :param size: размер футболики
    :param text: текст который будет напечатан на футболке.
    :return:
    """
    print(f"Вы заказали футболку размер {size}, c следующим текстом '{text}'")

make_shirt(27, "Я люблю PYTHON")# вызов с позиционными аргументами
make_shirt(size=31, text="Gibson forever")# вызов с именованными аргументами