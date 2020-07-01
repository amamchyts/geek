my_str = input('Введите строку с элементами через пробел ')
string = (my_str.split(' '))
x = len(string)
y = 0
while True:
    if len(string[y]) <= 10:
        print(string[y])
    else:
        z = (string[y])
        z = z[0:10]
        print(z)
    y = y + 1
    if y == x:
        break
