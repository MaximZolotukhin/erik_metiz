"""
Сэндвичи:
напишите функцию, которая получает список компонентов сэндвича. Функция должна иметь один
параметр для любого количества значений, переданных при вызове функции, и выводить описание
заказанного сэндвича. Вызовите функцию три раза с разным количеством аргументов.
"""
def make_sendvich(*topping):
    print("Мы делаем вам сендвичь из следующих компонентов: ")
    for sandvich in topping:
        print(f"- {sandvich}")
    print()

make_sendvich('сыр', 'колбаса', 'булочка')
make_sendvich('сыр', 'майонез', 'булочка', 'куриное филе', 'салат')
make_sendvich('булочка')