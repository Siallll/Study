x = 5
y = 10
print('x=', x, ' y=', y, sep="")
x = 5 + 5
y = 10 - 5
print('x=', x, ' y=', y, sep="")
tmp = x
x = y
y = tmp
print('x=', x, ' y=', y, sep="")
x, y = y, x
print('x=', x, ' y=', y, sep="")