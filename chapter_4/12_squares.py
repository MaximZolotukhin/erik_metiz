# Список номеров во второй степени
squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)

# Список номеров во второй степени варинат 2
squares_1 = [value**2 for value in range(1, 11)]
print(squares)
