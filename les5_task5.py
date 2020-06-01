with open('les5_task5.txt','w') as f_ile:
    print('1 22 45 45 1 21 212 2', file=f_ile)
with open('les5_task5.txt','r') as f_ile:
    s = f_ile.readline()
s = sum(list(map(int, s.split())))
with open('les5_task5_1.txt','w') as f:
    f.write(str(s))
