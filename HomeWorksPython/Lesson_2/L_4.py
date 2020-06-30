print('Вывод каждого слова с новой строки для введенного предложения.\n')

user_str = input("Введите предложение:\n")
idx = user_str.split(' ')
for i, el in enumerate(idx, 1):
    if len(el) > 10:
        el = el[0:10]
        print('{}. - {}'.format(i, el))
    else:
        len(el) == 0
        print('Вы ничего не ввели!')