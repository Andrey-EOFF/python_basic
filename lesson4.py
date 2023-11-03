a = 4
b = 6
c = (a + b) * 10
print (c)

a = 2
b = 3
c = (a + b) * 10
print (c)

print ('\n')

# FUNCTION PYTHON  ВАЖЛИВИЙ ВІДСТУП В РЯДКУ


def someFunction () :
    c = (a + b) * 10
    print (c)

a = 2
b = 3
someFunction()
a = 4
b = 5
someFunction()
a = 5
b = 6
someFunction()

print ('\n')
# глобальні значення

f = 66

def ex1 () :
    # global f
    f=44
    print (f)

ex1()
print (f)

print ('\n')

# аргументи

def ex2 (first, second) :
    c = (first + second) * 10
    print (c)

ex2 (2, 3)
ex2 (4, 6)
ex2 (5, 8)

def ex3 (s) :
    c = 'Hello ' + s
    print (c)

ex3 ('Mary')
ex3 ('Henry')

def ex4 (n, m) :
    result = n + m # 5
    return result

f = 100 + ex4(2, 3)
print (f)
print (ex4(100,200))

def ex5(n) :
    return n**2

print (ex5(5))
c = 100 + ex5(4)
print (c)


s = 4

def f03(s) :
    result = type(s)
    return result

print(f03(s))

num = 4.6

def f04(n) :
    result = round(n)
    print(result)


f04(num)

import random

def f05(a, b):
    return random.randint(a, b)
random_number = f05(1, 10)
print("Випадкове число:", random_number)

# Напишите функцию f06, которая возвращает значение из переменной a

a = 44444

def f06(a) :
    return a;

print(f06(a))

a = 101

def f07() :
    a = 100
    return a

print(f07())

a = 99

def f08() :
    global a
    
    return a

print(f08())
print(a)