age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age >= 65:
    price = 20
else:
    price = 40
print(f"Стоимость билета {price}")
