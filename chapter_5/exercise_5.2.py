"""
Больше условий: количество условий не ограничивается десятью. Попробуйте написать другие условия и включить их
в conditional_tests.py. Программа должна выдавать по крайней мере один истинный и один ложный результат
для следующих видов проверок:

    Проверка равенства и неравенства строк.

    Проверки с использованием функции lower().

    Числовые проверки равенства и неравенства, условий «больше», «меньше»,
    «больше или равно», «меньше или равно».

    Проверки с ключевым словом and и or.

    Проверка вхождения элемента в список.

    Проверка отсутствия элемента в списке.
"""
print("test")

string_1 = "python"
string_2 = "C++"
string_3 = "Python"
if string_1 != string_2:
    print("Строка не равны")

if string_1 == string_3:
    print("Строка равны")

if string_1.lower() == string_3.lower():
    print("Строка равны")

if 17 == 19:
    print("Числа равны")

if 17 <= 19:
    print("Условие равно")

if 17 >= 19:
    print("Условие равно")

if 17 > 19:
    print("Условие равно")

if 17 < 19:
    print("Условие равно")

if 17 <= 19 and 17 >= 14:
    print("Условие верно")

if 17 <= 12 or 17 >= 14:
    print("Условие верно")

list_persons = ["Рассомаха", "Супермен", "Человек паук", "Аквамен"]
super_hero = "Аквамен"

if super_hero in list_persons:
    print("Супергерой присутсвует в списке")

super_hero = "Бэтман"

if super_hero not in list_persons:
    print("Супергерой отсутсвует в списке")
