user_list = [7, 5, 3, 3, 2]

while True:
    user_element = input("Введите натуральное число - ")
    if user_element.isdigit():
        user_element = int(user_element)
        break
    print('Ввдено не число! Попробуйте еще раз.')

if user_element in user_list:
    user_list.insert(user_list.index(user_element), user_element)
elif not user_element:
    print(user_list)
elif user_list and user_element > max(user_list):
        user_list.insert(0, user_element)
else:
    user_list.append(user_element)
print(user_list)