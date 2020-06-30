print('Вывод каждого слова с новой строки для введенного предложения.\n')

user_str = input("Введите предложение:\n")
idx = user_str.split(' ')
empty = ''
for i, el in enumerate(idx, 1):
    if user_str == empty:
        empty = None
        print('Вы ничего не ввели!')
    else:
        len(el) > 10
        el = el[0:10]
        print('{}. - {}'.format(i, el))