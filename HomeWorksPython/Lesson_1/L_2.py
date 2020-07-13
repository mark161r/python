while True:
    user_time = input('Введите количество секунд:\n')
    if user_time.isdigit():
        user_time = int(user_time)
        break
    print('Ввдено не число! Попробуйте еще раз.')

hh = user_time // 3600
mm = (user_time % 3600) // 60
ss = (user_time % 3600) % 60

print("{:>02}:{:>02}:{:>02}".format(hh, mm, ss))