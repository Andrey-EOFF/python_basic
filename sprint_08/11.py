# itgid.info - python 2023

# Напишите функцию f11, которая принимает аргумент - list, и возвращает первое значение из list меньше нуля. Решите с помощью цикла.

# write your code under this line

def f11(lst):
    for elem in lst:
        if elem < 0:
            return elem

b = [8, -3, 5, 11, -2, 1, 15, 7]
result = f11(b)
print(result)
