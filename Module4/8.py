# Создайте эмуляцию работы магазина
# Класс Product должен содержать информацию о товаре: название, цена, количество на складе.
# Класс Customer должен содержать информацию о покупателе: имя, адрес, телефон.
# Класс Order должен содержать информацию о заказе: список товаров, покупатель, дата заказа.
# Класс Store должен управлять списком товаров и заказов, а также предоставлять
# методы для добавления товаров, создания заказов и отображения информации о заказах.


from datetime import datetime


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - {self.price} ( Остаток: {self.quantity})"


class Customer:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def __str__(self):
        return f"{self.name} - {self.address} ({self.phone})"


class Order:
    def __init__(self, customer, products):
        self.customer = customer
        self.products = products
        self.date_order = datetime.now()

    def __str__(self):
        product_str = ",".join([str(product) for product in self.products])
        return f"Заказ от {self.date_order.strftime('%Y-%m-%d %H:%M:%S')} \nПокупатель: {self.customer} \nТовары: {product_str} "


class Store:
    def __init__(self):
        self.products = []
        self.orders = []

    def add_product(self, product):
        self.products.append(product)

    def create_order(self, customer, products_names):
        products = [product for product in self.products if product.name in products_names]
        order = Order(customer, products)
        self.orders.append(order)
        return order

    def display_orders(self):
        for order in self.orders:
            print(order)

store = Store()

store.add_product(Product("Телефон", 15000, 10))
store.add_product(Product("Ноутбук", 45000, 5))

customer = Customer("Иван Иванов", "г.Москва, ул. Нахимовский проспект, 21", "+ 7 111 111 11 11")

order = store.create_order(customer, ["Телефон", "Ноутбук"])

store.display_orders()
