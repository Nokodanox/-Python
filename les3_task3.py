def my_f(arg_1, arg_2, arg_3):
    print(max((arg_1 + arg_2), (arg_2 + arg_3), (arg_1 + arg_3)))


a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
my_f(a, b, c)
