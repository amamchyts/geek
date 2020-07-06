def int_func():
    x = input('Введите строку ')
    x = (x.split(' '))
    i = 0
    while i < len(x):
        string = x[i]
        string_upper = string.capitalize()
        x[i] = string_upper
        i = i + 1
    print(' '.join(x))
int_func()