class Worker:
    name = None
    surname = None
    position = None
    __wage = None
    __bonus = None

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__wage = wage
        self.__bonus = bonus


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + self.surname

    def get_full_profit(self):
        self._income = {'profit': self.wage, 'bonus': self.bonus}
        return self._income


manager = Position('August', 'Swatr', 'manager', 500, 100)
print(manager.get_full_name(), manager.get_full_profit())
