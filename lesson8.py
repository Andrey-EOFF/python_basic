# Знайти суму елементів у List

def f01() :
    lst = [2,3,4,5,100,-50]
    s = 0
    i = 0
    while i < len(lst) :
        s = s + lst[i]
        i = i + 1
    print(s)

f01()

# Знайти суму елементів у List за допомогою цикла for in

def f02() :
    lst = [100, 200,-50]
    s = 0
    for item in lst :
        s = s + item
    print(s)

f02()

# Знайти добуток елементів у List за допомогою цикла for in

def f03() :
    lst = [2,3,2]
    p = 1
    for item in lst :
        p = p * item
    print(p)

f03()

# Знайти мінімальний елемент List

def f04() :
    lst = [2, 3, -3, 4, 55, 22, -1, -111]
    min = lst[0]
    for i in lst :
        if (i < min) :
            min = i
    print(min)        

f04()

# Знайти індекс!!! мінімального елемента у List

def f05() :
    lst = [2, 3, -3, 4, -55, 22, -1, 0]
    index = 0
    for i in range(len(lst)) :
        if (lst[i] < lst[index]) :
            index = i
    print(index)

f05()

# Знайти індекс!!! мінімального елемента у List

def f06() :
    lst = [200, 301, -3, 4, -7755, 22, -1, 0]
    index = 0
    i = 0
    while i < len(lst) :
        if (lst[i] < lst[index]) :
            index = i
        i = i + 1
    print(index)

f06()