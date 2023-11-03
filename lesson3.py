
#Вивод декількох значень

a=True
A=3.14

print(a)
print(A)

#Декілька змінних на одному рядку 

a, b, c, name = 1, 3, 100, "Alex"

print(a)
print(b)
print(c)
print(name)
print(a, b, c, name)

#string
#Довжина len

w='Hello'
t="Hello Omg"
print(w, t)
print(len(w))
print(len(t))

# Приводим тим данных руками, для того что бы не было ошибки

g= 3
k="stringtest"

print(str(g)+k) # переводим в строку

#Formating 

testword = "welcome"
sign="!"
print("Hello{} Python and {}! Are you ok".format(sign, testword))


n=4
v=13
print(v%n) #остаток
print(2**4) #степень
print(9**0.5) #корень
print(abs(-5)) #модуль числа