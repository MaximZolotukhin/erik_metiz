"""
Кошки и собаки:
создайте два файла с именами cats.txt и dogs.txt. Сохраните по крайней мере три клички кошек
в первом файле и три клички собак во втором. Напишите программу, которая пытается прочитать
эти файлы и выводит их содержимое на экран. Заключите свой код в блок try-except для перехвата
исключения FileNotFoundError и вывода понятного сообщения об отсутствии файла. Переместите один
из файлов в другое место файловой системы; убедитесь в том, что код блока except выполняется как
положено.
"""
filepath_cat = "cat.txt"
filepath_dog = "dog.txt"

def open_file(filename):
    try:
        with open(filename, 'r', encoding='UTF=8') as f:
            print(f"В фалйе {filename} следующие имена:")
            for name in f:
                print(f"{name}", end=' ')
            print("\n")
    except FileNotFoundError:
        print("Данного файла не найдено")

open_file(filepath_cat)
open_file(filepath_dog)
