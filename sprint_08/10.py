# itgid.info - python 2023

# Напишите функцию f10, которая принимает аргумент - list, и возвращает индекс первого встреченного значения list меньше нуля. Решите с помощью цикла.

# write your code under this line

def f10(lst):
    for index, elem in enumerate(lst):
        if elem < 0:
            return index
    return None

b = [8, 3, -5, -11, 2, -1, 15, 7]
result = f10(b)
print(result)
