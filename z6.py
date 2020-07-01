y = 0
z = 0
magaz = []
name_str = []
price_str = []
value_str = []
type_str = []
while True:
    vybor = str(input('Введите 1, для внесения нового товара и 0 для остановки: '))
    if vybor == '1':
        name_item = str(input('Введите категорию товара '))
        price_item = str(input('Введите цену товара '))
        value_item = str(input('Введите количество товара '))
        type_item = str(input('Введите параметр измерения '))
        spek = dict(key_name_item=name_item, key_price_item=price_item, key_value_item=value_item, key_type_item=type_item)
        tuple1 = (y + 1, spek)
        magaz.append(tuple1)
        y = y + 1
    else:
        if y == 0:
            print('Спасибо, досвидания')
        else:
            while z < y:
                magaz_str1 = magaz[z]
                magaz_str2 = magaz_str1[1]
                name_str.append(magaz_str2.get('key_name_item'))
                price_str.append(magaz_str2.get('key_price_item'))
                value_str.append(magaz_str2.get('key_value_item'))
                type_str.append(magaz_str2.get('key_type_item'))
                z = z + 1
            magaz_dict = dict (Name = name_str, Price = price_str, Value = value_str, Type = type_str)
            print(magaz_dict)
            print('Спасибо, что воспользовались нашими услугами!')
        break
