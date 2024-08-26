import random
import time


class TrafficLight:
    def __init__(self, color='red', timer=10):
        self.color = color
        self.timer = timer
        self.vehicles = []

    def change_color(self):
        if self.color == 'red':
            self.color = 'yellow'
        elif self.color == 'green':
            self.color = 'red'
        elif self.color == 'yellow':
            self.color = 'green'
        self.update_vehicle_speeds()

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        vehicle.traffic_light = self

    def remove_vehicle(self, vehicle):
        self.vehicles.remove(vehicle)
        vehicle.traffic_light = None

    def update_vehicle_speeds(self):
        for vehicle in self.vehicles:
            vehicle.update_speed()


class Vehicle:
    def __init__(self, vehicle_type, speed):
        self.vehicle_type = vehicle_type
        self.speed = speed
        self.traffic_light = None

    def update_speed(self):
        if self.traffic_light.color == 'red':
            self.speed = 0
        elif self.traffic_light.color == 'yellow':
            self.speed = random.randrange(1, 5)
        elif self.traffic_light.color == 'green':
            self.speed = random.randrange(10, 50)

    def move(self):
        if self.speed > 0:
            print(f"{self.vehicle_type} движется со скоростью {self.speed} км/ч")
        else:
            print(f"{self.vehicle_type} остановился на светофоре")
