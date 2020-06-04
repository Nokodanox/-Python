class Road:
    _lenght = None
    _width = None
    weight = None
    thickness = None

    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width
        print('Crate road_place object')

    def intake(self):
        self.weight = 25
        self.thickness = 1
        intake = self._width * self.weight * self.thickness * self._lenght / 1000
        print(f'Need {intake} ton for the building')


road_place = Road(2000, 5)
road_place.intake()