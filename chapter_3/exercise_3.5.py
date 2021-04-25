name_list = ['Максим', 'Ольга', 'Мирослава', 'Демид', 'Евгений']

print(f'{name_list[0]} приглашаю тебя на обед')
print(f'{name_list[1]} приглашаю тебя на обед')
print(f'{name_list[2]} приглашаю тебя на обед')
print(f'{name_list[3]} приглашаю тебя на обед')
print(f'{name_list[4]} приглашаю тебя на обед')
print(end="\n")

del_person = name_list.pop(4)
print(f'{name_list[0]} приглашаю тебя на обед')
print(f'{name_list[1]} приглашаю тебя на обед')
print(f'{name_list[2]} приглашаю тебя на обед')
print(f'{name_list[3]} приглашаю тебя на обед')
print(f'на обед не придет {del_person}')

name_list.append('Василий')
print(f'{name_list[0]} приглашаю тебя на обед')
print(f'{name_list[1]} приглашаю тебя на обед')
print(f'{name_list[2]} приглашаю тебя на обед')
print(f'{name_list[3]} приглашаю тебя на обед')
print(f'{name_list[4]} приглашаю тебя на обед')

