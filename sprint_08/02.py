# itgid.info - python 2023

# Напишите функцию f02, которая принимает аргумент - list, и возвращает произведение его элементов. Решите с помощью цикла.

# write your code under this line

def f02 (list) :
    total = 1
    for i in list :
        total = total * i
    return total    


b = [1, 2, 3]
result = f02(b)
print (result)
