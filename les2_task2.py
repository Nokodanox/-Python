lst = input('Введите данные для списка через пробел: ').split()
print(lst)
l = 0
for i in range(int(len(lst)/2)):
    lst[l], lst[l+1] = lst[l+1], lst[l]
    l += 2
print(lst)
