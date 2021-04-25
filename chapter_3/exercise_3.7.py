print('На обед приглашены всего 4 человека')

name_list = ['Максим', 'Ольга', 'Мирослава', 'Демид', 'Евгений', 'Валерий', 'Ирина', 'Илья']

print(f'{name_list.pop()} сожалею, но обед придется перенести')
print(f'{name_list.pop()} сожалею, но обед придется перенести')
print(f'{name_list.pop()} сожалею, но обед придется перенести')
print(f'{name_list.pop()} сожалею, но обед придется перенести')

print(f'{name_list[0]} приглашаю тебя на обед')
print(f'{name_list[1]} приглашаю тебя на обед')
print(f'{name_list[2]} приглашаю тебя на обед')
print(f'{name_list[3]} приглашаю тебя на обед')

del name_list[3]
del name_list[2]
del name_list[1]
del name_list[0]

print(name_list)
