# Task 09
# Напишите функцию f09, которая принимает строку - пароль, и возвращает True если длина пароля меньше 8 и False в противном случае.

def f09(p):
    if len(p) < 8 : 
        return True
    else :
        return False

print(f09('sddfdfddwd'))