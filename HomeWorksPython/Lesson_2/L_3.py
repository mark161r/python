print('Определение к каму времени года относиться номер месяца\n')

seasons_dict = {'Зима': (1, 2, 12),
                'Весна': (3, 4, 5),
                'Лето': (6, 7, 8),
                'Осень': (9, 10, 11)}

season_list = ['Зима', 'Весна', 'Лето', 'Осень']

while True:
    month = input('Введите число месяца:\n')
    if month.isdigit():
        month = int(month)
        break
    print('Ввдено не число! Попробуйте еще раз.')

if month == 1 or month == 2 or  month == 12:
    print('Время года из списка - ',season_list[0])
elif month == 3 or month == 4 or  month == 5:
    print('Время года из списка - ',season_list[1])
elif month == 6 or month == 7 or  month == 8:
    print('Время года из списка - ',season_list[2])
elif month == 9 or month == 10 or  month == 11:
    print('Время года из списка - ',season_list[3])
else:
    month <= 0 or month >= 13
    print('Месяца с таким номером не существует!')

for key in seasons_dict.keys():
    if month in seasons_dict[key]:
        print('Время года из словаря - ',key)



