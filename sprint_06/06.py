# itgid.info - python 2023

# Напишите функцию f06, которая получает число x, y и формирует строку от x до y (включительно оба числа). Число x всегда больше y. Шаг - три. Разделитель - знак "подчеркивания". Выводит строку в консоль.

# например f06 (12, 27) ожидаем в out строку _12_15_18_21_24_27

# write your code under this line
def f06 (x, y) :
    out = ""
    while x <= y :
        out += "_" + str(x)
        x += 3
    print (out)
    
f06(12, 27)
