motorcycles = ['Harley-Davidson', 'Suzuki', 'Kawasaki', 'honda', 'Ducati', 'Yamaha']
print(motorcycles)

''' 
Значение через remove можно удалить и с помощью переменной, 
чтобы в дальнейшем ее использовать для вывода сообщения о причине удаления
'''
too_exprensive = 'honda'
motorcycles.remove(too_exprensive)
print(motorcycles)
print(f'\nA {too_exprensive.title()} зарезервирован для Максима')