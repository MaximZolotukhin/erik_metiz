"""
Альбом:
напишите функцию make_album(), которая строит словарь с описанием музыкального альбома.
Функция должна получить имя исполнителя и название альбома для создания трех словарей,
представляющих разные альбомы. Выведите все возвращаемые значения, чтобы показать,
что информация правльно сохраняется во всех трех словарях.
Добавтьте в make_album() дополнительные параметры для сохранения количества дорожек в альбоме,
имеющие значения по умолчанию, добавьте это значение в словарь альбома. Создайте как минимум
один новый вызов функции с передачей количества дороже в альбом.
"""
# Функция создает словарь в соотвествии с переданными атрибутами
def make_album(name_musician, name_album, trek=''):
    if trek == '':
        make_album_dict = {'Название группы': name_musician, 'Название альбома': name_album}
    else:
        make_album_dict = {'Название группы': name_musician, 'Название альбома': name_album, 'количество треков': trek}
    return make_album_dict

# Сохраняем словари в перменные
Generator = make_album('Ария', "Генератор зла")
Lib_or_Death = make_album('GraveDigger', "Liberty or Death")
Koroli = make_album('Гран КуражЪ', "Короли, эпохи и судьбы", 13)

# Сохраняем переменные в список
list_albums= []
list_albums.append(Generator)
list_albums.append(Lib_or_Death)
list_albums.append(Koroli)

# Перебираем список и извлекаем из них информацию
for albums in list_albums:
    for name, values in albums.items():
        print(f"{name}: {values}")
    print('\n')