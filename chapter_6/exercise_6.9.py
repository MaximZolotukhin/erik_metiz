"""
Любимые места:
создайте словарь с именем favorite_places. Придумайте названия трех мест, которые станут
ключами словаря, и сохраните для каждого человека от одного до трех любимых мест.
Чтобы задача стала более интересной, опросите нескольких друзей и соберите реальные данные для своей
программы. Переберите данные в словаре, выведите имя каждого человека и его любимые места.
"""
# Создаем словарь c странами
favorite_places = {
    'Italia': 'Италия',
    'Petra': 'Петра',
    'Rome': 'Рим',
    'Atlantida': 'Атлантида',
    'Greece': 'Греция',
    'Egypt': 'Египет',
 }
# Создаем словарь с людей и присваиваем им места из списка стран
people = {
    'olga': {
        'places_1': favorite_places['Italia'],
        'places_2': favorite_places['Petra'],
        'places_3': favorite_places['Atlantida'],
    },
    'maxim': {
        'places_1': favorite_places['Italia'],
        'places_2': favorite_places['Rome'],
        'places_3': favorite_places['Greece'],
    },
    'vasilii': {
            'places_1': favorite_places['Egypt'],
        },
}
# Выводим результат, сначала общий и вложенным циклом перебираем присвоеные заначения стран
for name, places in people.items():
    print(f"{name.title()} хочет посетить: ")
    for place in places.values():
        print(f"{place.title()}", end=', ')
    print('\n')
