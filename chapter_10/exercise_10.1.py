"""
Изучение Python:
откройте пустой файл в текстовом редакторе и напишите несколько строк текста о возможностях Python.
Каждая строка должна начинаться с фразы «In Python you can…». Сохраните файл под именем learning_python.txt
в каталоге, использованном для примеров этой главы. Напишите программу, которая читает файл и выводит
текст три раза: с чтением всего файла, с перебором строк объекта файла и с сохранением строк в списке
с последующим выводом списка вне блока with.
"""

file_path = 'text_songs.txt'
# чтением всего файла
with open(file_path, encoding='utf-8') as file_object:
    content = file_object.read()
    print(content)
# с перебором строк объекта файла
with open(file_path, encoding='utf-8') as file_object:
    for str_file in file_object:
        content = str_file.rstrip()
        print(content)

print()
# с сохранением строк в списке с последующим выводом списка вне блока with
with open(file_path, encoding='utf-8') as file_object:
    content = file_object.readlines()

text_fool = ''
for str_text in content:
   text_fool += str_text

print(text_fool)
