def my_f():
    while True:
        a = int(input('Введите делимое: '))
        b = int(input('Введите делитель, который не равен 0: '))
        if b > 0:
            print(a // b)
            break
        else:
            print('На ноль делить нельзя.')
            my_f()

my_f()




