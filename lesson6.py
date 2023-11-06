def f ():
    i = 0
    while i <= 5 :
        i = i + 1
        print(i)
# f ()

def f01 (n) :
    out = ''
    i = 0
    while i <= n :
        out += str(i) + '_'
        i += 1 # i = i + 1
    print (out)


# f01(15)

def f02 (n) :
    out = ''
    i = n
    while i >= 0 :
        out += str(i) + '_'
        i = i - 2 # i -= 1
    print (out)

# f02(10)

def f03 () :
    out = ''
    i = 0
    while i < 10 :
        out +=  '*_'
        i = i + 1 
    print (out)

# f03()

def f04 () :
    out = ''
    i = 0
    while i < 10 :
        if i % 2 == 0 :
            out +=  '**_'
        else :
            out +=  '=_'
        i = i + 1 
    print (out)

# f04()

def f05 () :
    i = 5
    out = ''
    while i < 100 :
        if i > 11 :
            break
        out += str(i) + '_'
        i = i + 1
    print (out)

# f05()

def f06 () :
    i = 5
    out = ''
    while i < 20 :
        i = i + 1
        if i == 15 or i == 16:
            continue
        out += str(i) + '_'
    print (out)

f06()

