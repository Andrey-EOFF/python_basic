# itgid.info - python 2023

# Напишите функцию f08, которая формирует строку '*_*_*_*_*_*_*_*_*_*_'. Т.е. повторяет паттерн *_ причем количество раз зависит от аргумента n. Строка формируется циклом. Выводит строку в консоль.

# например f08(3) ожидаем в out строку *_*_*_

# write your code under this line

def f08 (n) :
    out = ""
    i = 1
    while i <= n : 
        out+= "*_"
        i+= 1
    print(out)    

f08(3) 

def f08(n):
    pattern = '*_'
    result = pattern * n
    print(result)


f08(3)

