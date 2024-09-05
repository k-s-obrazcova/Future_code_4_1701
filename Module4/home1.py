class Character:
    def __init__(self, name, health, damage):
        self._name = name
        self._health = health
        self._damage = damage

    def get_name(self):
        return self._name

    def get_health(self):
        return self._health

    def get_damage(self):
        return self._damage

    def take_damage(self, damage):
        self._health -= damage
        if self._health < 0:
            self._health = 0

    def attack(self, enemy):
        enemy.take_damage(self._damage)
        print(f"{self._name} атаковал {enemy.get_name} и нанес {self._damage} урона.")

class Warrior(Character):
    def __init__(self, name, health=100, damage=20):
        super().__init__(name, health, damage)

    def special_attack(self, enemy):
        damage = self.get_damage() * 1.5
        enemy.take_damage(damage)
        print(f"{self._name} ударил мечом {enemy.get_name} и нанес урон {damage}")

class Mage(Character):
    def __init__(self, name, health=70, damage=30):
        super().__init__(name, health, damage)


    def special_attack(self, enemy):
        damage = self.get_damage() * 2
        enemy.take_damage(damage)
        print(f"{self._name} ударил огненным шаром {enemy.get_name} и нанес урон {damage}")