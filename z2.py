my_list = input('Введите список с элементами через запятую ')
listing = (my_list.split(','))
x = len(listing)
if x % 2 == 0:
    print('в списке четное кол-во элементов')
else:
    print('в списке не-четное кол-во элементов')
    x = x - 1
y = 0
while True:
    m = listing[y]
    listing[y] = listing [y+1]
    listing[y+1] = m
    y = y + 2
    if y == x:
        break
print(listing)