import random

class Organism:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

    def get_food(self):
        pass

class Animal(Organism):
    def __init__(self, name, energy):
        super().__init__(name, energy)

    def hunt(self):
        pass

    def search_food(self):
        pass

    def reproduce(self):
        pass

class Predator(Animal):
    def hunt(self, prey):
        if random.random() > 0.5:  # 50% шанс, что хищник поймает добычу
            energy_spent = random.randint(5, 20)  # Случайная затраченная энергия
            if self.energy > prey.energy:
                self.energy += prey.energy - energy_spent
                prey.energy = 0
                print(f"{self.name} (Predator) hunted {prey.name} and now has {self.energy} energy.")
            else:
                print(f"{self.name} (Predator) failed to hunt {prey.name}.")
        else:
            print(f"{prey.name} (Prey) managed to escape from {self.name} (Predator).")

class Prey(Animal):
    def run_away(self):
        energy_spent = random.randint(1, 15)  # Случайная затраченная энергия
        self.energy -= energy_spent
        print(f"{self.name} (Prey) is running away and now has {self.energy} energy.")

class Ecosystem:
    def __init__(self):
        self.organisms = []

    def add_organism(self, organism):
        self.organisms.append(organism)

    def simulate_interaction(self):
        for organism in self.organisms:
            if isinstance(organism, Predator):
                for prey in self.organisms:
                    if isinstance(prey, Prey) and prey.energy > 0:
                        organism.hunt(prey)
                        break
            elif isinstance(organism, Prey):
                organism.run_away()

# Пример использования
ecosystem = Ecosystem()

# Добавляем хищника и добычу
predator = Predator("Lion", 50)
prey = Prey("Deer", 30)
ecosystem.add_organism(predator)
ecosystem.add_organism(prey)

# Симулируем взаимодействие
ecosystem.simulate_interaction()
