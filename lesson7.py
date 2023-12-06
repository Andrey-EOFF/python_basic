# Створення лістів (списків) у Python List

foo_1 = [11, 22, 33, 44]

# print(foo_1)

foo_2 = [22, 'Hello', True, 3.2]
# print(foo_2)

# звернення до одного елемента у List

print(foo_1[0])
print(foo_1[1])
print(foo_1[2])
print(foo_1[3])
# print(foo_1[4]) - помилка

# звернення до діапазону елементів у List

print('\n')

print(foo_1[1:3]) # 1,2
print(foo_1[1:]) # 1 - до кінця List
print(foo_1[:2]) # 0, 1

# перевіряємо наявність елемента у List
print('\n')

foo_1 = foo_1 = [11, 22, 33, 44]

print (333 in foo_1)
element = 44
print (element in foo_1)

if 'Hello' in foo_2 :
    print('Yes')
else :
    print('No')    