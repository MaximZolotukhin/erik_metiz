"""
Анализ лотереи:
напишите цикл, который проверяет, насколько сложно выиграть в смоделированной вами лотерее.
Создайте список или кортеж с именем my_ticket.
Напишите цикл, который продолжает генерировать комбинации до тех пор, пока не
выпадет выигрышная комбинация. Выведите сообщение с информацией о том, сколько
выполнений цикла понадобилось для получения выигрышной комбинации.
"""
from random import choice

tuple_loto = (1, 2, 5, 7, 'A', 3, 'E', 4, 'B', 'C', 6, 8, 'D', 9, 0)


def loto(numb_or_letter):
    """Функция выбирает из кортежа данные и сохраняет 4 символа в список"""
    flag_stop = True
    winning_values = []
    count = 1
    while flag_stop:
        value = choice(numb_or_letter)
        winning_values.append(value)
        if count == 4:
            flag_stop = False
        count += 1
    return winning_values

def select_win_combin(numb_or_letter, values_on_test):
    """Функция  Перебирает варинаты и узнает со скольки попыток была подобранная верная"""
    my_ticket = []
    count = 1
    # Использую два цикла один для создания комбинации цифр другой для сравнения.
    while True:
        for count_for in range(0, 4):
            value = choice(numb_or_letter)
            my_ticket.append(value)

        if values_on_test == my_ticket: # my_ticket = это эмуляция билета, values_on_test это выгрышнй номер.
            break
        else:
            my_ticket = []
            count += 1

    print(f"Комбинация подобранна с {count} попытки")


values = loto(tuple_loto)
print(f"Выгрышные номера {values}")
select_win_combin(tuple_loto, values)
