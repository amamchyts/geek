from itertools import count, cycle

# Задание №1

for el in count(5):
    if el <= 15:
        print(el, end=" ")
    else:
        break

# Задание №2

print("\n")
my_list = [el for el in range(3, 8)]
i = 0
pass_cycle = 0
for el in cycle(my_list):
    print(el, end=" ")
    i += 1
    if i == len(my_list):
        pass_cycle += 1
        i = 0
        print("\n")
    if pass_cycle == 2:
        break
