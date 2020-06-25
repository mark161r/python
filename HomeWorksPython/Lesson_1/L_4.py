print('Поиск наибольшего числа в строке из чисел')
while True:
    user_int = input('Введите строку из чисел:\n')
    if user_int.isdigit():
        user_int = int(user_int)
        break
    print('В строке есть буквы или спец. знаки! Попробуйте еще раз.')

tmp = user_int % 10
user_int = user_int // 10
while user_int > 0:
    if user_int % 10 > tmp:
        tmp = user_int % 10
    user_int = user_int // 10
print('Наибольшое число = {}'.format(tmp))

