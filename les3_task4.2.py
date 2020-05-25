def my_func(x, y):
    i = 0
    while i >= y:
        x = x / a
        i -= 1
    print(x)


a = float(input('x = '))
b = int(input('y = '))
#b = float(b)
my_func(a, b)

