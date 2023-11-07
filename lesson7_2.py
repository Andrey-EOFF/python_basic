# зміна List
def f01 () :
    bar = [11, 22, 33, 44]
    print (bar)
    bar[1] = 99
    print (bar)

# f01()

# зміна діапазона List
def f02 () :
    bar = [11, 22, 33, 44]
    print (bar)
    bar[0:2] = 88,99
    print (bar)

# f02()

# зміна діапазона List
def f03 () :
    bar = [11, 22, 33, 44]
    print (bar)
    # !!!!! [ ] 
    bar[0:2] = [88,99]
    print (bar)

# f03()

# зміна діапазона List - більше меньше
def f04 () :
    bar = [11, 22, 33, 44]
    print (bar)
    bar[0:2] = [88]
    print (bar)

# f04()

# замінюємо елемент без затирання
def f05 () :
    bar = [11, 22, 33, 44]
    print (bar)
    bar.insert(1, 88)
    print (bar)

f05()