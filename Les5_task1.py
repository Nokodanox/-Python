f_cool = input('Файл: ')
f = open(f_cool, 'w')
while 1:
    w = input()
    if w == '':
        break
    f.write(w + '\n')
f.close()