"""
Изменение списка гостей:
вы только что узнали, что один из гостей прийти не сможет, поэтому вам придется разослать
новые приглашения. Отсутствующего гостя нужно заменить кем-то другим.
    Начните с программы из упражнения 3.4. Добавьте в конец программы команду print для вывода имени гостя, который прийти не сможет.
    Измените список и замените имя гостя, который прийти не сможет, именем нового приглашенного.
    Выведите новый набор сообщений с приглашениями — по одному для каждого участника, входящего в список.
"""
# Создаем список имен
name_list = ['Максим', 'Ольга', 'Мирослава', 'Демид', 'Евгений']
# Приглашаем всех гостей согласно списка
print(f'{name_list[0]} приглашаю тебя на обед')
print(f'{name_list[1]} приглашаю тебя на обед')
print(f'{name_list[2]} приглашаю тебя на обед')
print(f'{name_list[3]} приглашаю тебя на обед')
print(f'{name_list[4]} приглашаю тебя на обед')
print(end="\n")
# Удаляем одного гостя и выводим всех гостей.
del_person = name_list.pop(4)
print(f'{name_list[0]} приглашаю тебя на обед')
print(f'{name_list[1]} приглашаю тебя на обед')
print(f'{name_list[2]} приглашаю тебя на обед')
print(f'{name_list[3]} приглашаю тебя на обед')
print(f'на обед не придет {del_person}')
print(end="\n")
# Добавляем еще одного гостя в конце списка
name_list.append('Василий')
print(f'{name_list[0]} приглашаю тебя на обед')
print(f'{name_list[1]} приглашаю тебя на обед')
print(f'{name_list[2]} приглашаю тебя на обед')
print(f'{name_list[3]} приглашаю тебя на обед')
print(f'{name_list[4]} приглашаю тебя на обед')
