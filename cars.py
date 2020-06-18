from pprint import pprint


class Car:
    hp = 160
    weight = 800  # kg
    mileage = 100  # km
    speed = 0  # km/h
    fuel = 100  # l
    state = 'stopped'
    position = 0
    price = 1000

    def __init__(self, color):
        self.color = color
        self.passengers = []

    def start(self):
        self.state = 'started'

    def stop(self):
        self.state = 'stopped'

    def accelerate(self, value):
        self.speed += value

    def drive(self, time):
        self.position += self.speed * time
        self.fuel -= time * 10  # l/h

    def __gt__(self, other):
        return self.speed > other.speed


class Expensive:
    price = 10000000

    def __init__(self):
        print('asdasd')


class Cabrio(Expensive, Car):
    hp = 260
    weight = 750  # kg

    def accelerate(self, value):
        super().accelerate(value)


car0 = Car('blue')
car0.accelerate(10)
car1 = Car('red')
car1.accelerate(20)
cabrio0 = Cabrio()

print(car0 < car1)
