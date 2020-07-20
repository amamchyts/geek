class Kletka:
    def __init__(self, kletka_number):
        self.data = kletka_number

    def __add__(self, second):
        return Kletka(self.data + second.data)
    def __sub__(self, second):
        return Kletka(self.data - second.data if self.data - second.data > 0 else print("Вычитание произвести невозможно"))
    def __mul__(self, second):
        return Kletka(self.data * second.data)
    def __truediv__(self, second):
        return Kletka(self.data // second.data)
    def make_order(self, param):
        string = ''
        for i in range(1, self.data + 1 + self.data // param):
            if i % (param + 1) != 0:
                string += '*'
            elif i != self.data + self.data // param:
                string += r'\n'
        return str(string.rstrip())

kletka_1 = Kletka(17)
kletka_2 = Kletka(14)

print((kletka_1 + kletka_2).data)
print((kletka_1 - kletka_2).data)
print((kletka_1 * kletka_2).data)
print((kletka_1 / kletka_2).data)
print(kletka_1.make_order(5))
print(kletka_2.make_order(5))