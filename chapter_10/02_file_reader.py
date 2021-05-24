# Чтение из файла с абслютным путем
file_path = f"E:\Python\python work\chapter_10\python_work\\text_files\info.txt"
with open(file_path, encoding='utf-8') as file_object:
    text_1 = file_object.read()

print(text_1)
