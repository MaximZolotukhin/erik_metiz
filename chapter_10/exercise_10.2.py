"""
Изучение C: метод replace() может использоваться для замены любого слова в строке другим словом.
В следующем примере слово 'dog' заменяется словом 'cat':

message = "I really like dogs."
message.replace('dog', 'cat')

'I really like cats.'
Прочитайте каждую строку из только что созданного файла learning_python.txt и замените слово
Python названием другого языка, например C. Выведите каждую измененную строку на экран.
"""

file_path = 'learning_python.txt'

with open(file_path, encoding='UTF8') as prog_lang:
    str_file = prog_lang.readlines()

for line_text in str_file:
    print(line_text.strip())
print('+_+'*20, end='\n')

for line_text in str_file:
    line_text.replace('Python', 'C++')
    print(line_text.replace('Python', 'C++').strip())
