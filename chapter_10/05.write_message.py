"Запись в пустой файл"
filename = 'programming.txt'

with open(filename, 'w', encoding='UTF-8') as file_object:
    file_object.write("Я люблю программировать.\n")
    file_object.write("Я люблю создавать игры.\n")
    file_object.write("Мне хочется работать программистом.\n")
