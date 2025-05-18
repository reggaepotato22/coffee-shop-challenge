class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self._customer = customer
        self._coffee = coffee

        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number")
        if price < 0:
             raise ValueError("Price cannot be negative")
        self._price = float(price)

        self._customer.add_order(self)
        self._coffee.add_order(self)

        Order.all.append(self)

    @property
    def price(self):
        return self._price

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @classmethod
    def all_orders(cls):
        return cls.all
