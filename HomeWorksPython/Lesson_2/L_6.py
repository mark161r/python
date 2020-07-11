need_new_item = 'да'
aincr = 1
goods = []

while need_new_item == 'да':
    # Заполняем данные по товару.
    item_name = input('Введите название товара: ')

    item_price = ''
    while not str.isdigit(item_price):
        item_price = input('Укажите цену товара: ')

    item_count = ''
    while not str.isdigit(item_count):
        item_count = input('Укажите кол-во: ')

    item_unit = input('Укажите ед. измерения: ')
    need_new_item = input('Хотите добавить еще один товар? (напишите `да` в случае согласия) ')