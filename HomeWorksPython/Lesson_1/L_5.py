print('Определение рентабельности компании.')

while True:
    u_vir = input('Введите выручку:\n')
    if u_vir.isdigit():
        u_vir = int(u_vir)
        break
    print('Ввдено не число! Попробуйте еще раз.')

while True:
    u_izd = input('Введите издержки:\n')
    if u_izd.isdigit():
        u_izd = int(u_izd)
        break
    print('Ввдено не число! Попробуйте еще раз.')

if u_vir > u_izd:
    while True:
        kol_sotr = input('Введите количество сотрудников в компании:\n')
        if kol_sotr.isdigit():
            kol_sotr = int(kol_sotr)
            break
        print('Ввдено не число! Попробуйте еще раз.')
    fin_r = u_vir / u_izd
    fin_p = u_vir - u_izd
    dahod_sotr = fin_p / kol_sotr
    print('\t', 'Фирма работает с прибылью, она состовляет = {}\n'.format(fin_p),
          '\t', 'Соотношение = {:>.1f}\n'.format(fin_r),
          '\t', 'Прибыль на одного сострудника равна = {:>.0f}'.format(dahod_sotr))
elif u_vir == u_izd:
    print('Фирма работает без убытков и даходов.')
else:
    print('Фирма работает в убыток!')