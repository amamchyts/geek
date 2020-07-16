class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def get_total_income(self):
            total_income = 0
            for value in self._income.values():
                total_income += value
            return total_income
    def get_full_name(self):
        return self.name + ' ' + self.surname

worker_1 = Position('Anton', 'Mamchyts', 'Student', {"wage": 50000, "bonus": 10000})

print(worker_1.get_full_name(),end=': ')
print(worker_1.get_total_income())


