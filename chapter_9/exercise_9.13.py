"""
Кубики:
создайте класс Die с одним атрибутом sides, который имеет значение по умолчанию 6.
Напишите метод roll_die() для вывода случайного числа от 1 до количества граней на кубике.
Создайте экземпляр, представляющий 6-гранный кубик, и смоделируйте 10 бросков.
Создайте экземпляры, представляющие 10- и 20-гранный кубик. Смоделируйте 10 бросков каждого кубика.
"""
import random

class Die():
    """
        Класс создает рандомное число
    """
    def __init__(self, sides):
        self.sides = sides # число граней кубика

    def roll_die(self):
        """Присваивает рандомное значение в заданном диапазоне"""
        result_roll_the_dice = random.randint(1, self.sides)
        return result_roll_the_dice


roll_the_dice_6 = Die(6)
roll_the_dice_10 = Die(10)
roll_the_dice_20 = Die(20)


def the_dice(example):
    count = 1
    while count <= 10:
        print(f"На кубике выпало число {example.roll_die()}")
        count += 1
    print("\n")

the_dice(roll_the_dice_6)
the_dice(roll_the_dice_10)
the_dice(roll_the_dice_20)
