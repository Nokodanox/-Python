from functools import reduce

def my_f(arg_1, arg_2):
    return arg_1 * arg_2


print(reduce(my_f, [i for i in range(100, 1001, 2)]))
