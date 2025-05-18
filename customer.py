
class Customer:
    def __init__(self, name):
        self.name = name  
        self._orders = [] 

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not 1 <= len(value) <= 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value

    def orders(self):
        from order import Order
        return [order for order in Order._all_orders if order.customer == self]

    def coffees(self):
        return list(set(order.coffee for order in self.orders()))

    def create_order(self, coffee, price):
        from order import Order
        from coffee import Coffee
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be a Coffee instance")
        order = Order(self, coffee, price)
        Order._all_orders.append(order)
        return order

    @classmethod
    def most_aficionado(cls, coffee):
        from order import Order
        from coffee import Coffee
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be a Coffee instance")
        coffee_orders = [order for order in Order._all_orders if order.coffee == coffee]
        if not coffee_orders:
            return None
        customer_spending = {}
        for order in coffee_orders:
            customer = order.customer
            customer_spending[customer] = customer_spending.get(customer, 0) + order.price
        return max(customer_spending, key=customer_spending.get)
