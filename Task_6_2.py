class Road:
    weight = 55
    thickness = 0.1

    def __init__(self, length: object, width: object) -> object:
        self._length = length
        self._width = width

    def calc(self) -> object:
        result = (self._length * self._width * Road.weight * Road.thickness) / 1000
        print(f'Need {result} tons of asphalt')


r_obj = Road(10, 5000)
r_obj.calc()
