# tuple не можна міняти - знак +

foo = (11, 22, 33)
bar = (44, 55, 66)

# foo += bar
# foo = foo + bar
foo = bar + foo

print(foo)

# del bar
print(bar)