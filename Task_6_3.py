class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

    def __str__(self):
        return f'Photograph {self.name} {self.surname} income is {self.get_total_income()}$'


p_obj = Position('Piter', 'Parker', 'photograph', 5000, 1000)
print(p_obj.get_full_name(), p_obj.get_total_income())
print(p_obj)