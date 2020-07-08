import math
def factorialische(n):
    for el in range(1, n+1):
        yield math.factorial(el)


n = int(input("Введите целое положительное число: "))

for i, el in enumerate(factorialische(n), 1):
    print(f'{i}! =', el)