prog_lang_list = ['assembler', 'c', 'c++', 'c#', 'php']
print(prog_lang_list)

prog_lang_list.append('python')
prog_lang_list.append('java script')
prog_lang_list.insert(0, '1c')
prog_lang_list.insert(8, '1c')
print(prog_lang_list)

prog_lang_list[8] = 'java'
prog_lang_list.insert(9, 'css')
print(prog_lang_list)

del prog_lang_list[8]
print(prog_lang_list)

prog_lang_list.pop()
del_valuse = prog_lang_list.pop(0)
print(prog_lang_list)
print(f'выл удален язык: {del_valuse}')

prog_lang_list.remove('php')
print(prog_lang_list, '\n')

print('Сортировка списка языков программирования')

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
