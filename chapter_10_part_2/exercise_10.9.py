"""
Ошибки без уведомления:
измените блок except из упражнения 10.8 так, чтобы при отсутствии файла
программа продолжала работу, не уведомляя пользователя о проблеме.
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
        pass

open_file(filepath_cat)
open_file(filepath_dog)
