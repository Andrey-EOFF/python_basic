# itgid.info - python 2023

# Напишите функцию f03, которая принимает аргумент - list, и возвращает cумму элементов list больше нуля. Решите с помощью цикла.

# write your code under this line

def f03 (lst) :
    total = 0
    for i in lst :
        if (i > 0) :
            total = total + i
    
    return total        


b = [1, -2, 4, 5, 2, 7, -11]
result = f03(b)
print (result)
