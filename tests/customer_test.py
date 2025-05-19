import unittest
from customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer1 = Customer("Alice")

    def test_customer_name_getter(self):
        self.assertEqual(self.customer1.name, "Alice")

    def test_customer_name_validation_length(self):
        with self.assertRaises(ValueError):
            Customer("A")
        with self.assertRaises(ValueError):
            Customer("ThisNameIsWayTooLongForValidation")

    def test_customer_name_validation_type(self):
        with self.assertRaises(TypeError):
            Customer(123)

    def test_customer_initial_orders_empty(self):
        self.assertEqual(self.customer1.orders(), [])

if __name__ == '__main__':
    unittest.main()
