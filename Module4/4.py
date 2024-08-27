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
        self.braking_distance = self.calculate_braking_distance()

    def calculate_weight(self):
        return self.engine.weight + self.fuel_tank.weight + self.brakes.weight + self.body.weight

    def calculate_max_range(self):
        return self.fuel_tank.volume * self.engine.max_speed / self.engine.fuel_consumption

    def calculate_braking_distance(self):
        return self.weight * self.brakes.effect


class Collector:
    def __init__(self):
        self.engine = None
        self.fuel_tank = None
        self.brakes = None
        self.body = None

    def set_engine(self, weight, max_speed, fuel_consumption):
        self.engine = Engine(weight, max_speed, fuel_consumption)

    def set_fuel_tank(self, weight, volume):
        self.fuel_tank = FuelTank(weight, volume)

    def set_brakes(self, weight, effect):
        self.brakes = Brakes(weight, effect)

    def set_body(self, weight):
        self.body = Body(weight)

    def build_car(self, name):
        return Car(name, self.engine, self.fuel_tank, self.brakes, self.body)


collector = Collector()
collector.set_engine(200, 40, 10)
collector.set_fuel_tank(100, 50)
collector.set_brakes(50, 0.5)
collector.set_body(500)
car = collector.build_car("MyCar")

print(car.name)
print(car.weight)
print(car.max_range)
print(car.braking_distance)