# tuple - не можна змінювати!!!!!!!!!
x = (11, 22, 33, 44)
# x[1] = 55

# tuple -> list
y = list(x)

y[1] = 555
y.append('ho ho ho')

# list -> tuple
x = tuple(y)

print(x)