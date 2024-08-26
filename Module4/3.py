import random
import time


class TrafficLight:
    def __init__(self, color='red', timer=10):
        self.color = color
        self.timer = timer
        self.vehicles = []

    def change_color(self):
        if self.color == 'red':
            self.color = 'green'
        elif self.color == 'green':
            self.color = 'yellow'
        elif self.color == 'yellow':
            self.color = 'red'
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

    def run(self):
        while True:
            print(f'Текущий цвет {self.color}')
            time.sleep(self.timer)
            self.change_color()



class Vehicle:
    def __init__(self, vehicle_type, speed=0):
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


traffic_light = TrafficLight(timer=5)
car = Vehicle('Машина')
truck = Vehicle('Грузовик')

traffic_light.add_vehicle(car)
traffic_light.add_vehicle(truck)

import threading
traffic_light_thread = threading.Thread(target=traffic_light.run)
traffic_light_thread.start()

while True:
    car.move()
    truck.move()
    time.sleep(1)