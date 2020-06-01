
with open('les5_task4.txt', 'r') as f_boot, open('les5_task4_1.txt', "w") as f_write:
    replace = {0: 'Один', 1: 'Два', 2: 'Три', 3: 'Четыре'}
    i = 0
    while True:
        if i <= 3:
            lines = f_boot.readline().split()
            lines[0] = replace[i]
            i += 1
            print(' '.join(lines), file=f_write)
        elif i == 4:
            break


#with open('les5_task4_1.txt', "w") as f_write:
   # f_write.write(str(lines))