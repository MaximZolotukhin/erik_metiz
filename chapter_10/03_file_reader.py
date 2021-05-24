# Перебор данных с помощью for
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)

# Сохранение данных в список.
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line)

# Вывод числа в одну строку .
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))