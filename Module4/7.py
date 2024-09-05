class GameObject:
    def __init__(self, x, y, width, height, name):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.name = name

    def update(self):
        self.x += 1
        self.y += 1
        print(f"Объект сместился на позиции {self.x} : {self.y}")


class Character(GameObject):
    def __init__(self, x, y, width, height, name, health):
        super().__init__(x, y, width, height, name)
        self.health = health

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        print(f"Персонаж переместился на позицию {self.x} : {self.y}")

    def interact(self, other):
        if isinstance(other, Item):
            print(f"Персонаж взаимодействует с предметом {other.name}")


class Enemy(Character):
    def __init__(self, x, y, width, height, name, health, attack_power):
        super().__init__(x, y, width, height, name, health)
        self.attack_power = attack_power

    def attack(self, target):
        target.health -= self.attack_power
        print(f"Враг нанес урон {self.attack_power}")

    def take_damage(self, damage):
        self.health -= damage
        print(f"Враг получил урон {damage}")


class Item(GameObject):
    def __init__(self, x, y, width, height, name):
        super().__init__(x, y, width, height, name)

    def use_item(self, target):
        if self.name == "Зелье":
            target.health += 20
            print(f"{target.name} использовал {self.name} и добавил 20 здоровья")


class GameWorld:
    def __init__(self):
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)
        print(f"Объект успешно добавлен")

    def handle_interactions(self):
        for obj in self.objects:
            if isinstance(obj, Character):
                for other in self.objects:
                    if obj != other:
                        obj.interact(other)

world = GameWorld()
hero = Character(0,0, 50, 50, "Павел", 100)
enemy = Enemy(100, 100, 50, 50, "Иван", 100, 20)
potion = Item(50, 50, 10, 10, "Зелье")


world.add_object(hero.name)
world.add_object(enemy.name)
world.add_object(potion.name)

hero.move(10,10)

hero.interact(potion)

enemy.attack(hero)

hero.interact(enemy)

potion.use_item(hero)

world.handle_interactions()