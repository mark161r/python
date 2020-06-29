print('Обмен значениями соседних элементов в списке заданном пользователем.\n')

user_s = input('Введите значения списка через пробел:\n')
print(user_s)
user_list = user_s.split('')

s = 0 #счетчик

while s < len(user_list[:-1]):
    user_list[s], user_list[s + 1] = user_list[s + 1], user_list[s]
    s += 2

print(user_list)