# Именованные аргументы.
# Тут используются параметры по умолчанию, он обязательно должнен стоят в конце.
def describe_pet(pet_name, animal_type="собака"):
    """
    Выводит информацию о животном.
    :param animal_type: вид животного
    :param pet_name: кличка животного
    :return:
    """
    print(f"\nУ меня есть {animal_type}")
    print(f"Кличка моей {animal_type} {pet_name.title()}")

describe_pet(pet_name="шелби") # Так как у нас установлен параметр по умолчанию, нет необходимости его пердовать в функцию.
describe_pet(animal_type="кошка", pet_name="сима") # Вызов функции с двумя параметрами.