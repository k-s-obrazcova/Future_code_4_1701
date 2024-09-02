class GameObject:
    def __init__(self, x, y, width, height, name):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.name = name

    def update(self):
        # Пример логики обновления состояния объекта
        self.x += 1
        self.y += 1
        print(f"GameObject updated: x={self.x}, y={self.y}")

class Character(GameObject):
    def __init__(self, x, y, width, height, health, strength, name):
        super().__init__(x, y, width, height, name)
        self.health = health
        self.strength = strength

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        print(f"Character moved to: x={self.x}, y={self.y}")

    def interact(self, other):
        # Пример логики взаимодействия с другим объектом
        if isinstance(other, Item):
            print(f"Character interacts with {other.name}")

class Enemy(Character):
    def __init__(self, x, y, width, height, health, strength, attack_power, name):
        super().__init__(x, y, width, height, health, strength, name)
        self.attack_power = attack_power

    def attack(self, target):
        target.health -= self.attack_power
        print(f"Enemy attacks {target} and deals {self.attack_power} damage")

    def take_damage(self, damage):
        self.health -= damage
        print(f"Enemy takes {damage} damage")

class Item(GameObject):
    def __init__(self, x, y, width, height, name):
        super().__init__(x, y, width, height, name)

    def use(self, target):
        # Пример логики использования предмета
        if self.name == "Health Potion":
            target.health += 20
            print(f"{target} uses {self.name} and gains 20 health")

class GameWorld:
    def __init__(self):
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)
        print(f"Object added: {obj}")

    # def update(self):
    #     for obj in self.objects:
    #         obj.update()

    def handle_interactions(self):
        # Пример логики обработки взаимодействий между объектами
        for obj in self.objects:
            if isinstance(obj, Character):
                for other in self.objects:
                    if obj != other:
                        obj.interact(other)

# Пример использования
world = GameWorld()
hero = Character(0, 0, 50, 50, 100, 10, "Pavel")
enemy = Enemy(100, 100, 50, 50, 50, 5, 10, "Mio")
potion = Item(50, 50, 10, 10, "Health Potion")

world.add_object(hero.name)
world.add_object(enemy.name)
world.add_object(potion.name)

# # Обновление мира
# world.update()

# Перемещение героя
hero.move(10, 10)

# Взаимодействие героя с предметом
hero.interact(potion)

# Атака врага на героя
enemy.attack(hero)

# Герой получает урон
hero.interact(enemy)

# Использование предмета героем
potion.use(hero)

# Обработка взаимодействий в мире
world.handle_interactions()
