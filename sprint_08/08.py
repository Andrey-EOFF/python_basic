# itgid.info - python 2023

# Напишите функцию f08, которая принимает аргумент - list, и возвращает максимальное значение из list. Решите с помощью цикла.

# write your code under this line

def f08 (lst) :
    max = 0
    for i in lst :
        if i > max :
            max = i
    return max        


b = [8, 2, -5, 11, 2, 1, 15, 3]
result = f08(b)
print (result)
