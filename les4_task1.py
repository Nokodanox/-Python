from sys import argv
name, worker_name, f_1, f_2, f_3 = argv
f_1 = int(f_1); f_2 = int(f_2); f_3 = int(f_3)
pr = f_1 * f_2 + f_3
print(name)
print('Введите имя сотрудника: ', worker_name)
print('Введите количество часов отработанных работником: ', f_1)
print('Введите ставку за час работника: ', f_2)
print('Введите премию работника: ', f_3)
print('Сотрудник: ' + worker_name + '. Заработная плата: ' + str(pr) + 'р.')

