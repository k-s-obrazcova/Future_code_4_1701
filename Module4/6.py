class MenuItem:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients


class Order:
    def __init__(self):
        self.items = []
        self.status = 'new'

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


class Restaurant:
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
            order.update_status('in process')
            # Here you can add more logic for processing the order
            order.update_status('completed')


# Создаем экземпляр ресторана
restaurant = Restaurant()

# Добавляем блюда в меню
restaurant.add_menu_item(MenuItem("Пицца", 8.99, ["тесто", "сыр", "томатный соус", "пепперони"]))
restaurant.add_menu_item(MenuItem("Салат Цезарь", 5.99, ["салат", "курица", "пармезан", "соус Цезарь"]))

# Добавляем столики
restaurant.add_table(1)
restaurant.add_table(2)

# Добавляем заказ для столика 1
table_1 = restaurant.tables[1]
table_1.current_order.add_item(restaurant.menu[0])  # Пицца
table_1.current_order.add_item(restaurant.menu[1])  # Салат Цезарь

# Рассчитываем общую сумму заказа для столика 1
total = table_1.current_order.calculate_total()
print(f"Общая сумма заказа для столика 1: {total} EUR")

# Обрабатываем заказ для столика 1
restaurant.process_order(1)
print(f"Статус заказа для столика 1: {table_1.current_order.status}")

# Удаляем блюдо из меню
restaurant.remove_menu_item("Пицца")
print("Меню после удаления Пиццы:")
for item in restaurant.menu:
    print(f"- {item.name}: {item.price} EUR")
