"""
Отправка сообщений:
начните с копии вашей программы из упражнения 8.9. Напишите функцию send_messages(),
которая выводит каждое сообещние и перемещает его в новый список с именем sent_messages.
После вызова функции выведите оба списка и убедитесь в том, что в исходном списке остались
все сообщения.
"""

# Создаем списки
short_messages = ['Привет', 'Как дела?', 'Подь сюды', 'Куды прешь леший']
sent_messages = []
# Функция переносит из одного списк в дургой информацию
def send_messages(short_messages, sent_messages):
    while short_messages:
        mess = short_messages.pop()# удаляем сообщения из первого списка сохраняя его во второй список
        sent_messages.append(mess)# добавляем ко второму списку


def print_list(short_messages, sent_messages):
    """
    Выводит в терминал первый и второй список
    :param short_messages:
    :param sent_messages:
    :return:
    """
    print(short_messages, end="\n")
    print(sent_messages)


send_messages(short_messages, sent_messages) # short_messages[:] передает копию списка
print_list(short_messages, sent_messages)

