my_list = [7, 5, 3, 3, 2]
new_item = int(input('Введите новую отметку рейтинга '))
lenth = len(my_list)
y = 0
while True:
    if new_item >= int(my_list[y]):
        my_list.insert(y, new_item)
        break
    else:
        if new_item >= int(my_list[y+1]):
            y = y + 1
        else:
            my_list.append(new_item)
            break
print(my_list)