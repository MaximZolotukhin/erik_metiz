"""
Пользовательские альбомы:
начните с программы из упражнения 8.7. Напишите программу цикл
while, в котором пользователь вводит исполнителя и название альбома. Затем в цикле
вызывается функция make_album() для введенных пользователей и выводится созаднный
словарь. Не забудь предусмотреть признак завершения в цикле while
"""

# Функция создает словарь в соотвествии с переданными атрибутами
def make_album(name_musician, name_album, trek=''):
    if trek == '':
        make_album_dict = {'Название группы': name_musician, 'Название альбома': name_album}
    else:
        make_album_dict = {'Название группы': name_musician, 'Название альбома': name_album, 'количество треков': trek}
    return make_album_dict

# Цикл взаимодействия с пользователем.
list_albums = [] # Создаю новый список
while True:
    musician_group = input("Введите название группы: ")
    name_album = input("Введите название албома: ")
    quit_while = input("Если хотите завершить ввод данных нажмите 'q': ")
    list_albums.append(make_album(musician_group, name_album, trek='')) # Сохраняю данные в список
    if quit_while == 'q':
        print("\n")
        break
    else:
        continue


# Перебираем список и извлекаем из них информацию
for albums in list_albums:
    for name, values in albums.items():
        print(f"{name}: {values}")
    print('\n')
