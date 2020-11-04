a = float(input('Результат в первый день: '))
b = float(input('Целевой результат: '))
day = 1
while a <= b:
    a *= 1.1
    day += 1
else:
    print(f'На {day}-й спортсмен достиг цели - не менее {b} км' )