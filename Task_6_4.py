class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'The {self.name} is went!'

    def stop(self):
        return f'The {self.name} is stopped!'

    def turn_left(self):
        return f'The {self.name} is turn_left!'

    def turn_right(self):
        return f'The {self.name} is urn_right!'

    def show_speed(self):
        return f'The {self.name} is moving at normal speed'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'The {self.name} is moving at over speed'
        else:
            return f'The {self.name} is moving at normal speed'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'The {self.name} is moving at over speed'
        else:
            return f'The {self.name} is moving at normal speed'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


LADA = SportCar(100, 'Black', 'Lada Priora', False)
UAZ = TownCar(30, 'Green', 'UAZ Patriot', True)
Mazeratti = WorkCar(70, 'Yellow', 'Mazeratti', False)
ZAZ = PoliceCar(110, 'Blue',  'ZAZ Change', True)

print(f'{LADA.name} a police car? {LADA.is_police}')
print(f'{ZAZ.name} a police car? {ZAZ.is_police}')

print(LADA.turn_left())
print(UAZ.turn_right())
print(Mazeratti.stop())
print(ZAZ.go())
print(Mazeratti.show_speed())
print(ZAZ.show_speed())