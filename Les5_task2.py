f_cool = open('les5_task2.txt', 'r')
line = 0
for i in f_cool:
    line += 1
    word = 0
    pos = 'out'
    for a in i:
        if a != ' ' and pos == 'out':
            word += 1
            pos = 'in'
        elif a == ' ':
            pos = 'out'
    print(word, ' сл. в строке.')
print(line, ' строк.')
f_cool.close()