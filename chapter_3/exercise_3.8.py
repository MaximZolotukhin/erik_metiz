contry = ['canada', 'greece', 'japan', 'egypt', 'hawaii']
print(contry)
print('*' * 33)

print('Временная сортировка списка по алфавиту')
print(sorted(contry))
print(contry)
print('*' * 33)

print('Временная сортировка списка по алфавиту в обратном порядке')
print(sorted(contry, reverse=True))
print(contry)
print('*' * 33)

print('Реверс списка')
reversed(contry)
print(contry)
reversed(contry)
print(contry)
print('*' * 33)

print('Постоянная сортировка списка по алфавиту')
contry.sort()
print(contry)

print('Постоянная сортировка списка по алфавиту в обратном порядке')
contry.sort(reverse=True)
print(contry)
