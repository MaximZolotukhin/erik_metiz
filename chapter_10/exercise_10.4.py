"""
Гостевая книга:
напишите цикл while, который запрашивает у пользователей имена. При вводе каждого имени
выведите на экран приветствие и добавьте строку с сообщением в файл с именем guest_book.txt.
Проследите за тем, чтобы каждое сообщение размещалось в отдельной строке файла.
"""
guest_book = "guest_book.txt"
name_guest = 'y'

with open(guest_book, 'a', encoding='UTF-8') as guest_list:
    while True:
        name_guest = input("Введите имя гостя: ")
        if name_guest == 'n':
            break
        guest_list.write(f"{name_guest}\n")
