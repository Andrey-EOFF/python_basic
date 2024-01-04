# itgid.info - python 2023

# Напишите функцию f01, которая принимает аргумент - list, и возвращает сумму его элементов. Решите с помощью цикла.

# write your code under this line

def f01 (lst) :
    total = 0
    for elem in lst:
        total += elem
    return total


b = [ 11, -3, 4, 12, 7, -8]
result = f01(b)
print (result)
