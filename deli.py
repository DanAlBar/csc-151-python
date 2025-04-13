print("\nWelcome to The Carolina Deli!")

sandwich_orders = ["tuna", "chicken", "veggie", "club", "ham and cheese"]

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nAll sandwiches have been made! Here is your order:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.capitalize()} Sandwich")
