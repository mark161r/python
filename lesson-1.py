while True:
    user_time = input('введите количество секунд\n')
    if user_time.isdigit():
        user_time = int(user_time)
        break

    print('ввдено не число')

    hh = user_time / 3600
    mm = (user_time % 3600) / 60
    ss = (user_time % 3600) % 60


print(f'{hh:>02}:{mm:>02}:{ss:>02}')
print("{:>02}:{:>02}:{:>02}".format(hh, mm, ss))