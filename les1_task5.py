revenue = int(input('Введите прибыль: '))
cost = int(input('Введите издержки: '))
if revenue - cost < 0:
    print('Ваша фирма работает в убыток.')
elif revenue - cost > 0:
    print('Ваша фирма получает прибыль.')
    revenue_rent = (revenue - cost) / revenue
    print('Рентабельность выручки составляет ' + str(revenue_rent) + ' %.')
    personal = int(input('Введите количество персонала: '))
    revenue_personal = (revenue - cost) / personal
    print('Прибыль фирмы при расчете на одного сотрудника ' + str(revenue_personal))
else:
    print('Ваша фирма работает в 0.')
