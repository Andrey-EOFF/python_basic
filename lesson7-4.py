# вивід у консоль за допомогою цикли for

def f01 () :
    list = [11, 22, 33, 44, 55]
    out = ''
    for item in list :
        out += str(item) + ','
    print (out)
    
# f01()        

# вивід у консоль з індексами

def f02 () :
    list = [11, 22, 33, 44, 55]
    out = ''
    i = 0
    while i < len(list) :
        out += str(i) +' -> '+ str(list[i]) + '\n'
        i += 1
    print (out)

# f02()    

# вивід у консоль з індексами

def f03 () :
    foo = [22, 33, 44, 55]
    out = ''
    for i in range(len(foo)) :
        out += str(i) +' -> '+ str(foo[i]) + '\n'
        i += 1
    print (out)

# f03()        

def f12(lst, item):
    lst.append(item)
    return lst

m12 = [11, 22]
result = f12(m12, 55)
print(result)