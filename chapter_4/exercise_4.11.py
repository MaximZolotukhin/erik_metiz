"""
Моя пицца, твоя пицца:
начните с программы из упражнения 4.1. Создайте копию списка с видами пиццы, присвойте ему имя friend_pizzas.
Затем сделайте следующее:

    Добавьте новую пиццу в исходный список.

    Добавьте другую пиццу в список friend_pizzas.

    Докажите, что в программе существуют два разных списка. Выведите сообщение «My favorite pizzas are:»,
    а затем первый список в цикле for. Выведите сообщение «My friend’s favorite pizzas are:»,
    а затем второй список в цикле for. Убедитесь в том, что каждая новая пицца находится
    в соответствующем списке.
"""
metall_group_list = ['Ария', 'Гран Куражъ', 'Iron Maiden', 'Metallica']
frend_group = metall_group_list[:]

metall_group_list.append('Sabbaton')

frend_group.append('Garve Digger')

print('Мои любимые группы')
for group in metall_group_list:
    print(group)

print('\n')
print('Любимые группы друга')
for group in frend_group:
    print(group)
