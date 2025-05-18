class Customer:
    all = []

    def __init__(self, name):
        self.name = name
        self._orders = []
        Customer.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not (1 <= len(name) <= 15):
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = name

    def add_order(self, order):
        self._orders.append(order)

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set([order.coffee for order in self._orders]))

    @classmethod
    def all_customers(cls):
        return cls.all
