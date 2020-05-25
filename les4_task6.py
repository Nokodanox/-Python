from itertools import count, islice, cycle

n = input('n = ')
while True:
    try:
        n = int(n)
        break
    except ValueError:
        n = input('Введите корректное число: ')

for i in islice(count(n), 5):
    print(i)
print('Задание 2:')
b = [i for i in range(1, 5)]
for i in islice(cycle(b), 10):
    print(i)