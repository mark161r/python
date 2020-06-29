user_s = input('Введите список через запятую:\n')
print(user_s)
user_list = user_s.split(',')
print(user_list)

s = 0 #счетчик

while s < len(user_list[:-1]):
    user_list[s], user_list[s + 1] = user_list[s + 1], user_list[s]
    s += 2
    print(user_list)