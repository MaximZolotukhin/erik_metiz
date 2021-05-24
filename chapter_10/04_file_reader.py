#Проверяем входил ли дата рождения в первый миллион цифр числа P
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

brithday = input("Введите день вашего рождения: ")
if brithday in pi_string:
    print("День вашего рождения зашифрован в первом миллионе символов числа Pi")
else:
    print("День вашего рождения отсутсвует в первом миллионе символов числа Pi")
