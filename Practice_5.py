proceeds = int(input('Укажите прибиль: '))
costs = int(input('Укажите издержки: '))

result = proceeds - costs

if result > 0:
    print('Ваша прибыль составила: ', result)
    print(f'Рентабельность выручки: {proceeds / costs}')
    employees = int(input('Укажите сколько у Вас сотрудников: '))
    print(f'Вы получили {result / employees} на каждого сотрудника')
elif result == 0:
    print('Вы не получили прибыли')
else:
    print('Вы понесли убытки: ', -result)