def t01 ():
    a = 7
    b = 10
    c = 0

    if a > 6 :
        c = a * b
        c = c + 3

    print (c)
    
# t01 ()

def t02 () :
    a = 6
    if a % 2 == 0:
        print ("even")
    else:
        print("odd")    
   
# t02()

def t03 () :
    color = 44
    
    if color == 1 :
        trafficLight = "green"
    elif color ==2 :
        trafficLight = "yellow"
    elif color ==3 :
        trafficLight = "red"
    else :
        trafficLight = "blink yellow"    
    print (trafficLight)    

  

# t03()

def t04 () :
    user = 'mask'
    password = 'tuxedo1'

    if user == 'mask' and password == 'tuxedo1' :
        print ('welcome')
    else :
        print ('wrong')

t04()

# ==
# >
# <
# >=
# <=
# !=
# and - обидві умови!!!
# or - будь яка умова!!!
