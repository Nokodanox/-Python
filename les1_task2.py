time = int(input('Введите необходимое для перевода время: '))
time_hour = time // 3600
time = time % 3600
time_min = time // 60
time_sec = time % 60
time_hour = str(time_hour); time_min = str(time_min); time_sec = str(time_sec)
if len(time_min) == 1:
    time_min='0' + time_min
if len(time_sec) == 1:
    time_sec='0' + time_sec
print(time_hour + ':' + time_min +  ':' + time_sec)
