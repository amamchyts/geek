from sys import argv
_, hours, price, bonus = argv
def pay_money(hours, price, bonus):
    cash = (float(hours) * float(price) + float(bonus))
    print('Необходимо выплатить', cash)
pay_money(hours, price, bonus)
