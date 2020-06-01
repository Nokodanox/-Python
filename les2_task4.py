a = input('Введите через пробел: ').split()
n = 1; n = int(n)
l = 0
for i in range(len(a)):
    print(str(n) + '.' + str(a[l][0:10]))
    n += 1; l += 1