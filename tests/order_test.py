import unittest
from order import Order
from customer import Customer
from coffee import Coffee

class TestOrder(unittest.TestCase):

    def setUp(self):
        self.customer1 = Customer("Alice")
        self.coffee1 = Coffee("Espresso", "Dark Roast")
        self.order1 = Order(self.customer1, self.coffee1, 3.50)

    def test_order_price_getter(self):
        self.assertEqual(self.order1.price, 3.50)

    def test_order_customer_getter(self):
        self.assertEqual(self.order1.customer, self.customer1)

    def test_order_coffee_getter(self):
        self.assertEqual(self.order1.coffee, self.coffee1)

    def test_order_price_validation_type(self):
        with self.assertRaises(TypeError):
            Order(self.customer1, self.coffee1, "free")

    def test_order_price_validation_negative(self):
        with self.assertRaises(ValueError):
            Order(self.customer1, self.coffee1, -1.00)

if __name__ == '__main__':
    unittest.main()
