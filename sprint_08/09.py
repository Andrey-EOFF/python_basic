# itgid.info - python 2023

# Напишите функцию f09, которая принимает аргумент - list, и возвращает минимальное значение из list. Решите с помощью цикла.

# write your code under this line

def f09(lst) :
    min = lst[0]
    for i in lst :
        if i < min :
            min = i
    return min        


b = [8, 3, 5, 11, 2, 1, 15, 7, -7]
result = f09(b)
print (result)
