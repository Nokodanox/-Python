a = int(input('Результат первого дня: '))
b = int(input('Желаемый результат: '))
n = 1
print('Результат ' + str(n) + ' дня: ' + str(round(a, 2)))
while a < b:
    a = a + (a / 100 * 10)
    n = n + 1
    print('Результат ' + str(n) + ' дня: ' + str(round(a, 2)))
print('На ' + str(n) + '-й день, спортсмен достиг результата - не менее ' + str(round(a, 2)) + ' км.')


