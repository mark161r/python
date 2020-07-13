print('Добавление числа в рейтинг и вывод.\n')

rating_list = [7, 5, 3, 3, 2]

while True:
    user_element = input("Введите натуральное число - ")
    if user_element.isdigit():
        user_element = int(user_element)
        break
    print('Ввдено не число! Попробуйте еще раз.')

if user_element in rating_list_list:
    rating_list_list.insert(rating_list_list.index(user_element), user_element)
elif not user_element:
    print(rating_list)
elif rating_list_list and user_element > max(rating_list):
        rating_list.insert(0, user_element)
else:
    rating_list.append(user_element)
print(rating_list)