# itgid.info - python 2023

# Напишите функцию f04, которая принимает аргумент - list, и возвращает cумму четных элементов данного list. Решите с помощью цикла.

# write your code under this line

def f04(lst):
    total_even = 0
    for elem in lst:
        if elem % 2 == 0:
            total_even += elem
    return total_even

b = [1, -2, 4, 5, 2, 7, -11]
result = f04(b)
print(result)
