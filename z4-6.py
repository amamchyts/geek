class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)
    def go(self):
        print('Машина двигается')
    def stop(self):
        print('Машина стоит')
    def turn(self, direction):
        print(f'Машина изменила направление на {direction}')
    def show_speed(self):
        print(f'Скорость автомобиля {self.name} состовляет {self.speed} км/ч')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость автомобиля {self.name} превышает 60 км/ч')
        else:
            print(f'Скорость автомобиля {self.name} состовляет {self.speed} км/ч')
class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость автомобиля {self.name} превышает 40 км/ч')
        else:
            print(f'Скорость автомобиля {self.name} состовляет {self.speed} км/ч')
class PoliceCar(Car):
    def police(self):
        if self.is_police:
             print("За вами идет преследование")

my_town_car = TownCar(80, 'Серебристый', 'Киа', False)
my_sport_car = SportCar(349, 'золотой', 'БМВ', False)
my_work_car = WorkCar(55, 'серый', 'ГАЗель', False)
my_police_car = PoliceCar(80, 'полицейская ливрея', 'Форд', True)

print(my_town_car.color)
print(my_sport_car.name)
print(my_police_car.is_police, '\n')

my_sport_car.go()
my_sport_car.turn("право")
my_sport_car.stop()

my_sport_car.show_speed()
my_police_car.show_speed()
my_town_car.show_speed()
my_work_car.show_speed()
my_police_car.police()