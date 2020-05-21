def my_f(a):
    a = a.split()
    if 'q' in map(str, a):
        a.remove('q')
    b = []
    for i in a:
        b.append(int(i))
    return sum(b)


s = 0
while 1:
    a = input('Для прекращения работы программы введите "q": ')
    if 'q' in map(str, a):
        s += my_f(a)
        print('Сумма: ', s)
        break
    s += my_f(a)
    print('Сумма: ', s)