def my_func(num1, num2):
   y = abs(num2)
   i = 1
   x = 1
   while i <= y:
       x = x * num1
       i = i + 1
   x = 1 / x
   print(x)
my_func(2,2)