def my_func():
    sum_X_all = 0
    i = 0
    while True:
        x = input('Введите последовательность, S - для остановки ')
        if x[len(x) - 1] != 'S':
            x = (x.split(' '))
            sum_X = 0
            while i < len(x):
                 sum_X = sum_X + int(x[i])
                 i = i + 1
            i = 0
            sum_X_all = sum_X_all + sum_X
            print(sum_X_all)
        else:
            print(sum_X_all)
            break
my_func()