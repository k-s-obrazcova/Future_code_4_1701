class Engine:
    def __init__(self, weight, max_speed, fuel_consumption):
        self.weight = weight
        self.max_speed = max_speed
        self.fuel_consumption = fuel_consumption


class FuelTank:
    def __init__(self, weight, volume):
        self.weight = weight
        self.volume = volume


class Brakes:
    def __init__(self, weight, effect):
        self.weight = weight
        self.effect = effect


class Body:
    def __init__(self, weight):
        self.weight = weight


class Car:
    def __init__(self, name, engine, fuel_tank, brakes, body):
        self.name = name
        self.engine = engine
        self.fuel_tank = fuel_tank
        self.brakes = brakes
        self.body = body
        self.weight = self.calculate_weight()
        self.max_range = self.calculate_max_range()
        self.braking_distance

    def calculate_weight(self):
        return self.engine.weight + self.fuel_tank.weight + self.brakes.weight + self.body.weight

    def calculate_max_range(self):
        return self.fuel_tank.volume * self.engine.max_speed / self.engine.fuel_consumption

    def calculate_braking_distance(self):
