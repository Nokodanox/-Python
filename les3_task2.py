def userInfo(name , sename , old , live_in , email , number ):
    print(str('Пользователь: ' + name + ' ' + sename + ', возраст ' + old + ', место проживания: ' + live_in + ', электронная почта: ' + email + ', номер: ' + number))

name = input('Введите ваше имя: ')
sename = input('Введите вашу фамилию: ')
old =  input('Введите ваш возраст: ')
live_in = input('Введите ваше место проживания: ')
email = input('Введите вашу электронную почту: ')
number = input('Введите ваш номер телефона: ')

userInfo(name=name , sename=sename , old=old , live_in=live_in , email=email , number=number )

