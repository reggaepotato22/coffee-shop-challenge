# debug.py (Simplified)

from customer import Customer
from coffee import Coffee
from order import Order

print("--- Creating Instances ---")

customer1 = Customer("Alice")
customer2 = Customer("Bob")

coffee1 = Coffee("Espresso", "Dark Roast")
coffee2 = Coffee("Latte", "Vanilla")

order1 = Order(customer1, coffee1, 3.50)
order2 = Order(customer1, coffee2, 4.00)
order3 = Order(customer2, coffee1, 3.50)

print("Instances created.")
print("-" * 20)

print("--- Demonstrating Relationships ---")

print(f"{customer1.name}'s orders:")
for order in customer1.orders():
    print(f"  - Ordered {order.coffee.name} for {order.price}")

print(f"{customer1.name}'s unique coffees ordered:")
for coffee in customer1.coffees():
    print(f"  - {coffee.name}")

print(f"Orders for {coffee1.name}:")
for order in coffee1.orders():
    print(f"  - Ordered by {order.customer.name} for {order.price}")

print(f"Customers who ordered {coffee1.name}:")
for customer in coffee1.customers():
    print(f"  - {customer.name}")

print(f"\n{coffee1.name} - Total Orders: {coffee1.num_orders()}")
print(f"{coffee1.name} - Average Price: {coffee1.average_price():.2f}")


print("-" * 20)
print("Debug session finished.")
