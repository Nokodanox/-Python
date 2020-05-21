def my_f(a):
    while True:
        if a != a.lower():
            a = input('Введите символы в нижнем регистре: ')
        else:
            break
    print(a.title())


a = str(input('a = '))
my_f(a)