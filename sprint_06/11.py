# itgid.info - python 2023

# Напишите функцию f11, находит и ВОЗВРАЩАЕТ сумму целых чисел от 0 до n. Где n - аргумент функции. 

# например f11(4) функция возвращает число 10, потому что в диапазоне числа 0 + 1 + 2 + 3 + 4


# write your code under this line

def f11(n):
    total = sum(range(n + 1))
    return total

result = f11(4)
print (result)

