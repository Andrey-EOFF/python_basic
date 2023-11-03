import random

# itgid.info - python 2023
# Task 10
# Напишите функцию f10, которая возвращает сумму global переменных a, b.

a = 99
b = 1

def f10() :
    global a
    global b
    return a+b

print(f10())
