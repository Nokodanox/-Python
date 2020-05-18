my_list = [7, 5, 3, 3, 2]
a = int(input('Введите число: '))
for i in range(len(my_list)):
    if a in my_list:
        n = my_list.index(a)
        if n > max(my_list):
            my_list.insert(0, a)
            break
        if n < min(my_list):
            my_list.append(a)
        else:
            clon = (my_list.count(a))
            my_list.insert(n + clon, a)
            break
print(my_list)
