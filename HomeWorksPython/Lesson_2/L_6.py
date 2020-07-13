print('Составление списка товаров.\n')

need_new_item = 'да'
numb_item = 1
price = []

while need_new_item == 'да':
    item_name = input('Введите наименование товара: ')

    item_price = ''
    while not str.isdigit(item_price):
        item_price = input('Введите цену товара: ')

    item_count = ''
    while not str.isdigit(item_count):
        item_count = input('Введите кол-во: ')

    item_unit = input('Введите ед. измерения: ')
    item = (numb_item,
            {
                'наименование': item_name,
                'цена': item_price,
                'количество': item_count,
                'ед. изм.': item_unit
            }
            )
    price.append(item)
    numb_item += 1
    need_new_item = input('Хотите добавить еще один товар? (напишите `да/нет`) - ')

statistic = {}

for item in price:
    item_data = item[1]
    for key in item_data:
        if (not statistic.get(key)):
            statistic[key] = []
        if statistic[key].count(item_data[key]):
            continue
        statistic[key].append(item_data[key])

print(f'Список товаров: {price}')
print(f'Статистика по товарам: {statistic}')