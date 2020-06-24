my_int = 7
my_float = 12.3
my_str = 'Переменная строка'
print('\t', my_int, '\n', '\t', my_float, '\n', '\t', my_str)
print('\t', type(my_int), '\n', '\t', type(my_float), '\n', '\t', type(my_str))
my_int_2 = input('Введите число которое будет отображено после ввода:\n')

if my_int_2.isdigit():
    my_int_2 = int(my_int_2)
else:
    print('Вы ввели не число!')
print(my_int_2)

my_str2 = input('Введите слово или предложение которое будет отображено после ввода:\n')
print(my_str2)
