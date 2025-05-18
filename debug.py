from customer import Customer
from coffee import Coffee
from order import Order

# --- Create Instances ---
print("--- Creating Instances ---")

# Create a customer
customer1 = Customer("Alice")

# Creates a coffee typee
coffee1 = Coffee("Latte", "Vanilla")

# Creates an order
order1 = Order(customer1, coffee1, 4.00)

print("Instances created.")
print("-" * 20)

print("--- Demonstrating Relationship ---")

# customer's name from the order
print(f"Order 1 was placed by: {order1.customer.name}")

# coffee name from the order
print(f"Order 1 was for: {order1.coffee.name}")

# orders for the customer
print(f"{customer1.name}'s orders:")
for order in customer1.orders():
    print(f"  - {order.coffee.name} (Price: {order.price})")

print("-" * 20)
print("Simple debug session finished.")
