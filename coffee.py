class Coffee:
    all = []

    def __init__(self, type, name):
        if not isinstance(type, str):
            raise TypeError("Coffee type must be a string")
        if not (1 <= len(type) <= 15):
            raise ValueError("Coffee type must be between 1 and 15 characters")
        self._type = type

        if not isinstance(name, str):
            raise TypeError("Coffee name must be a string")
        if not (1 <= len(name) <= 15):
            raise ValueError("Coffee name must be between 1 and 15 characters")
        self._name = name

        self._orders = []

        Coffee.all.append(self)

    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return self._type

    def add_order(self, order):
        self._orders.append(order)

    def orders(self):
        return self._orders

    def customers(self):
        return list(set([order.customer for order in self._orders]))

    @classmethod
    def all_coffees(cls):
        return cls.all

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        orders = self._orders
        if not orders:
            return 0.0
        total_price = sum(order.price for order in orders)
        return total_price / len(orders)
