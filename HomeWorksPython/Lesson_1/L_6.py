print('Определение дня при котором спортсмен достигнет нужного результата при пробежке.')
while True:
    s_km = input('Введите количество киллометров за первый день:\n')
    if s_km.isdigit():
        s_km = int(s_km)
        break
    print('Ввдено не число! Попробуйте еще раз.')

while True:
    g_res = input('Введите количесвто килломентров являющееся целью:\n')
    if g_res.isdigit():
        g_res = int(g_res)
        break
    print('Ввдено не число! Попробуйте еще раз.')

res_day = 1
res_km = s_km

while res_km <= g_res:
    res_km = res_km + res_km * 0.1
    res_day += 1

print('Результат будет достигнут на {} день'.format(res_day))