# itgid.info - python 2023

# Напишите функцию f06, которая принимает аргумент - list, и возвращает произведение элементов, значение которых меньше 10. Решите с помощью цикла.

# write your code under this line

def f06(lst):
    total = 1
    for elem in lst:
        if elem < 10:
            total *= elem
    return total

b = [1, 2, 5, 11, 2, 1, 15, 3, 15]
result = f06(b)
print(result)