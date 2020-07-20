from abc import ABC, abstractmethod
class ABS_Palto(ABC):
    @abstractmethod
    def __init__(self, size):
        pass

class ABS_Kostyum(ABC):
    @abstractmethod
    def __init__(self, height):
        pass

class ABS_Odezhda(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def itog(self):
        pass

    @abstractmethod
    def new_item(self, type, size_of_type):
        pass


class Palto(ABS_Palto):
    def __init__(self, itog):
        self.itog = itog / 6.5 + 0.5


class Kostyum(ABS_Kostyum):
    def __init__(self, itog):
        self.itog = 2 * itog + 0.3


class Odezhda(ABS_Odezhda):
    def __init__(self):
        self.odezhda = []
    def new_item(self, type, size_of_type):
        if type == 'Palto':
            self.odezhda.append(Palto(size_of_type))
            print(f'Успешно добавлен экземпляр {type} с параметром {size_of_type}')
        elif type == 'Kostyum':
            self.odezhda.append(Kostyum(size_of_type))
            print(f'Успешно добавлен экземпляр {type} с параметром {size_of_type}')
        else:
            print("Такой одежды нет")

    @property
    def itog(self):
        itog = 0
        for el in self.odezhda:
            itog += el.itog
        return itog


my_clothes = Odezhda()
my_clothes.new_item('Palto', 1)
my_clothes.new_item('Kostyum', 6.5)
my_clothes.new_item('Rubashka', 6.5)
print("Итого ткани: ", my_clothes.itog)
