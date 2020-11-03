time = int(input('Введите время (сек): '))

# 1 - sec
# 60 - min
# 3600 - hour
# 86400 - day

if time <= 86400:
    hour = time // 3600
    min = time // 60 % 60
    sec = time % 60
    if sec < 10 and hour < 10 and min < 10:
        print(f'Текущее время: 0{hour % 24}:0{min}:0{sec}')
    elif sec < 10 and hour < 10:
        print(f'Текущее время: 0{hour % 24}:{min}:0{sec}')
    elif sec < 10 and min < 10:
        print(f'Текущее время: {hour % 24}:0{min}:0{sec}')
    elif min < 10 and hour < 10:
        print(f'Текущее время: 0{hour % 24}:0{min}:{sec}')
    else:
        print(f'Текущее время: {hour % 24}:{min}:{sec}')
else:
    print('Вы взорвали временно-пространственный континуум')
