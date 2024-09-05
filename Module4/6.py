from time import sleep


class MenuItem:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients


class Order:
    def __init__(self):
        self.items = []
        self.status = 'New'

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        return sum(item.price for item in self.items)

    def update_status(self, status):
        self.status = status


class Table:
    def __init__(self, table_number):
        self.table_number = table_number
        self.current_order = Order()


class Restaurant():
    def __init__(self):
        self.menu = []
        self.tables = {}

    def add_menu_item(self, item):
        self.menu.append(item)

    def remove_menu_item(self, item_name):
        self.menu = [item for item in self.menu if item.name != item_name]

    def add_table(self, table_number):
        self.tables[table_number] = Table(table_number)

    def remove_table(self, table_number):
        if table_number in self.tables:
            del self.tables[table_number]

    def process_order(self, table_number):
        if table_number in self.tables:
            order = self.tables[table_number].current_order
            order.update_status('In process')
            sleep(2)
            order.update_status('Complete')


restaurant = Restaurant()

restaurant.add_menu_item(MenuItem("Пицца", 800, ["тесто", "сыр", "ветчина"]))
restaurant.add_menu_item(MenuItem("Салат Цезарь", 560, ["салат", "курица", "соус цезарь", "пармезан"]))

restaurant.add_table(1)
restaurant.add_table(2)

table_1 = restaurant.tables[1]
table_1.current_order.add_item(restaurant.menu[0])
table_1.current_order.add_item(restaurant.menu[1])

total = table_1.current_order.calculate_total()
print(f"Общая сумма заказа для стола 1: {total}")

restaurant.process_order(1)
print(f"Статус заказа для столика 1: {table_1.current_order.status}")

restaurant.remove_menu_item("Пицца")
print("Меню после удаления Пиццы:")
for item in restaurant.menu:
    print(f"- {item.name}: {item.price} РУБ")
