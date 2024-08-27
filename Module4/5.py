import random


class Organism:
    def __init__(self, name, energy, type_hunter):
        self.name = name
        self.energy = energy
        self.type_hunter = type_hunter


class Animal(Organism):
    def __init__(self, name, energy, type_hunter):
        super().__init__(name, energy, type_hunter)

    def hunt(self, prey):
        pass

    def search_food(self):
        pass


class Predator(Animal):
    def hunt(self, prey):
        if random.random() > 0.5:
            energy_spent = random.randint(5, 20)
            if self.energy > prey.energy:
                self.energy += prey.energy - energy_spent
                prey.energy = 0
                print(f"{self.name} поймал {prey.name} и сейчас имеет {self.energy} энергии")
            else:
                print(f"{self.name} упустило {prey.name}")
        else:
            print(f"{self.name} не нашел {prey.name}")

    def search_food(self):
        print(f"{self.name} является хищником и ищет добычу")


class Prey(Animal):
    def run_away(self):
        energy_spent = random.randint(1, 15)
        self.energy -= energy_spent
        print(f"{self.name} сбежал от хищника")

class Ecosystem:
    def __init__(self):
        self.organisms = []

    def add_organism(self, organism):
        self.organisms.append(organism)

    def interaction(self):
        for organism in self.organisms:
            if isinstance(organism, Predator):
                for prey in self.organisms:
                    if isinstance(prey, Prey) and prey.energy > 0:
                        organism.hunt(prey)
                        break

ecosystem = Ecosystem()

predator = Predator("Лев", 50, "Млекопитающие")
prey = Prey("Олень", 30, "Трава")
ecosystem.add_organism(predator)
ecosystem.add_organism(prey)

ecosystem.interaction()
