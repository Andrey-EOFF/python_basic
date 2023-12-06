# додаємо елементи у кінець List
def f01 () :
    foo = [11, 22, 33, 44]
    print (foo)
    foo.append(55)
    foo.append(66)
    
    print (foo)

# f01()

# розширення List за рахунок іншого
def f02 () :
    foo = [11, 22, 33, 44]
    bar = [55, 66, 77]
    foo.extend(bar)
    print (foo)

# f02()

# видаляємо елементи List
def f03 () :
    foo = [11, 22, 33, 44, 55, 66]
    print (foo)
    foo.pop()
    print (foo)
    foo.pop(1)
    print (foo)
    del foo[1]
    print (foo)

# f03()

# очищаємо List
def f04 () :
    foo = [11, 22, 33, 44, 55, 66]
    print (foo)
    foo = []
    print (foo)
    ##############
    foo = [11, 22, 33, 44, 55, 66]
    print (foo)
    foo.clear()
    print (foo)

# f04()