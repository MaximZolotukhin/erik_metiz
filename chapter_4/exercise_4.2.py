"""
Животные:
    создайте список из трех (и более) животных, обладающих общей характеристикой.
    Используйте цикл for для вывода названий всех животных.

    Измените программу так, чтобы вместо простого названия выводилось сообщение, включающее это название,
    — например, «A dog would make a great pet».

    Добавьте в конец программы строку с описанием общего свойства. Например, можно
    вывести сообщение «Any of these animals would make a great pet!».
"""
list_animal = ['Кошка', 'Собака', 'Медведь', 'Волк', 'Бык']

for animal in list_animal:
    print(f'Мне нравится {animal}')

print('У всех животных четыре лапы')
