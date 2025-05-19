import unittest
from coffee import Coffee

class TestCoffee(unittest.TestCase):

    def setUp(self):
        self.coffee1 = Coffee("Espresso", "Dark Roast")

    def test_coffee_name_getter(self):
        self.assertEqual(self.coffee1.name, "Dark Roast")

    def test_coffee_type_getter(self):
        self.assertEqual(self.coffee1.type, "Espresso")

    def test_coffee_type_validation_length(self):
        with self.assertRaises(ValueError):
            Coffee("A", "Name")
        with self.assertRaises(ValueError):
            Coffee("ThisTypeIsWayTooLongForValidation", "Name")

    def test_coffee_name_validation_length(self):
        with self.assertRaises(ValueError):
            Coffee("Type", "N")
        with self.assertRaises(ValueError):
            Coffee("Type", "ThisNameIsWayTooLongForValidation")

    def test_coffee_type_validation_type(self):
        with self.assertRaises(TypeError):
            Coffee(123, "Name")

    def test_coffee_name_validation_type(self):
        with self.assertRaises(TypeError):
            Coffee("Type", 123)

    def test_coffee_initial_orders_empty(self):
        self.assertEqual(self.coffee1.orders(), [])

if __name__ == '__main__':
    unittest.main()
