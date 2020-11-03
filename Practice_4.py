integer = int(input('Введите целое положительное число: '))
print('Число: ', integer)
max = 0

if integer > 0:
    while integer % 10 or integer // 10:
        if max < integer % 10:
            max = integer % 10
            integer = integer // 10
        else:
            integer = integer // 10
else:
    print('Число отрицательное')

print('Максимальное: ', max)