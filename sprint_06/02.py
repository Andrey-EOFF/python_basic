# itgid.info - python 2023

# С помощью цикла while создайте переменную out, где будет лежать строка вида '5_6_7_8_9_'. Выведите в консоль out.  Шаг - единица.

# write your code under this line

out = ""
i = 5

while i <= 9 :
    out = out + str(i) + "_"
    i = i + 1

print (out)