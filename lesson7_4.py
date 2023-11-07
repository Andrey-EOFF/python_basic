# вивід у консоль за допомогою цикли for
def f01 () :
    foo = [22, 33, 44, 55]
    out = ''
    for item in foo:
        out += str(item) + '_'
    print (out)

# f01()

# вивід у консоль з індексами
def f02 () :
    foo = [22, 33, 44, 55]
    out = ''
    i = 0
    while i < len(foo) : 
        out += str(i) +' -> '+ str(foo[i]) + '\n'
        i = i + 1
    print (out)

# f02()

# вивід у консоль з індексами
def f03 () :
    foo = [22, 33, 44, 55]
    out = ''
    for i in range(len(foo)) :
        out += str(i) +' - '+ str(foo[i]) + '\n'
        i = i + 1
    print (out)

f03()