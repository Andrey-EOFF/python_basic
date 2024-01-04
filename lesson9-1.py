# як ми створювали list
lst = [22, 33, 44]
print( type(lst) )

# створюємо кортеж tuple
tpl = (77, 88, 99, 100)
print (type(tpl))

# схожі - індекси
print (lst[1])
print (tpl[1])

# схожі - len
print (len(lst))
print (len(tpl))

# схожі - містити дублікати

foo = ['hello', 1, 2, 'hello']
bar = ('hi', 44, 55, 66, 'hi')

print(foo)
print(bar)

print('\n =========================\n')

# різниця tuple - не можна змінювати
foo[1] = 555
print(foo)

# bar[1] = 555 # помилка