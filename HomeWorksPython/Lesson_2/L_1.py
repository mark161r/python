print('Вывод типов различных данных из списка.\n')
print('Сам список:')
list1 = [25, -123, None, 'Srt', True, 3.14, [1, 2]]
print(list1,'\n')
print('Соответствие типов:')
for i in list1:
    print('{} является типом {}'.format(i, type(list1)))