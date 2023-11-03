# Task 07
# Напишите функцию f07, которая принимает знак (+, - , / , *) и возвращает результат математической операции примененной к переменным a, b. Обратите внимание - переменные созданы внутри функции.

def f07(s, a, b):
    if s == '+':
        return a + b
    elif s == '-':
        return a - b
    elif s == '*':
        return a * b
    elif s == '/':
        return a / b


a = 10
b = 5
operation = '/'
result = f07(operation, a, b)
print("Результат операції:", result) 