"""
Сегменты:
Добавьте в конец одной из программ, написанных в этой главе, фрагмент, который делает следующее:

    Выводит сообщение «The irst three items in the list are:», а затем использует сегмент для вывода
    первых трех элементов из списка.

    Выводит сообщение «Three items from the middle of the list are:», а затем использует сегмент для
    вывода первых трех элементов из середины списка.

    Выводит сообщение «The last three items in the list are:», а затем использует сегмент для
    вывода последних трех элементов из списка.
"""
prog_lang_list = ['assembler', 'c', 'c++', 'c#', 'java script']

print('Выводим первый три строчки списка')
print(prog_lang_list[:3])

print('Выводим первые три сторочик из середины списка')
print(prog_lang_list[1:4])

print('Выводим первый три строчки с конца списка')
print(prog_lang_list[-3:])
