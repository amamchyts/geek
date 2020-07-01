my_list = ['apple', 2020, 15.6, False, [10, 20]]
x = len(my_list)
y = 0
while True:
    print(type(my_list[y]))
    y = y + 1
    if y == x:
        break
