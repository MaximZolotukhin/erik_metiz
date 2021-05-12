# Возвращение словаря
def build_person(first_name, last_name, age=''):
    """ Возвращение словаря с информацие о человеке. """
    person = {'first': first_name, 'last': last_name} # Создание словаря
    if age:
        person['age'] = age # Добавление в словарь еще одного параметра.
    return person


musician = build_person('jimi', 'hendrix', age=27)
print(musician)
