print('Расчет задачи по формуле x+xx+xxx')
while True:
    user_int = input('Введите число:\n')
    if user_int.isdigit():
        user_int = int(user_int)
        break
    print('Ввдено не число! Попробуйте еще раз.')

result = int(user_int) + int(user_int * 2) + int(user_int * 3)
print('Результат = {}'.format(result))