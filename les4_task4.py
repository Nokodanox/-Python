import random
a = [random.randrange(1,50,1) for i in range(20)]
print(a)
#a = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
b = []
for i in a:
    if a.count(i) == 1:
        b.append(i)
print(b)