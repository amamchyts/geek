class Road:
    def __init__(self, length, width):
        self._length = int(length)
        self._width = int(width)

    def MassCalc(self):
            asphalt_mass = int(input('Введите массу асфальта для покрытия одного кв метра дороги толщиной в 1 см '))
            heigh = int(input('Введите толщину слоя '))
            massa = asphalt_mass * heigh * self._width * (self._length * 0.01)
            print('Для покрытия всего дорожного полотна необходимо ', int(massa/1000), 'тонн')

length = 20
width = 5000

my_MassCalc = Road(length, width)
my_MassCalc.MassCalc()


