"""
Все функции:
придумайте информацию, которую можно было бы хранить в списке.
Например, создайте список гор, рек, стран, городов, языков... словом,
чего угодно. Напишите программу, которая создает список элементов, а затем
вызвает каждую функцию, упоминавшуюся в этой главе, хотя бы один раз.
"""
# Создаем список
prog_lang_list = ['assembler', 'c', 'c++', 'c#', 'php']
print(prog_lang_list)

# Добавляем языки программирования в конец списка
prog_lang_list.append('python')
prog_lang_list.append('java script')
# Добавляем языки по индексу с помощью insert
prog_lang_list.insert(0, '1c')
prog_lang_list.insert(8, '1c')
print(prog_lang_list)

prog_lang_list[8] = 'java'
prog_lang_list.insert(9, 'css')
print(prog_lang_list)

# Удаляем 9 позицию из списка
del prog_lang_list[8]
print(prog_lang_list)
# Удаляем позицию в конце списка
prog_lang_list.pop()
# Сохраняем удаленные данные
del_valuse = prog_lang_list.pop(0)
print(prog_lang_list)
print(f'выл удален язык: {del_valuse}')
# Удаляем данные по значению
prog_lang_list.remove('php')
print(prog_lang_list, '\n')

print('Сортировка списка языков программирования')
# Сортируем список по алфавиту
print(sorted(prog_lang_list))
print(sorted(prog_lang_list, reverse=True), '\n')

print('Реверс списка языков программирования')
prog_lang_list.reverse()
print(prog_lang_list)
prog_lang_list.reverse()
print(prog_lang_list, '\n')

prog_lang_list.sort()
print(prog_lang_list)
prog_lang_list.sort(reverse=True)
print(prog_lang_list)
