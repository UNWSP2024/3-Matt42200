BEGIN
    DISPLAY "Enter your age: "
    INPUT age


    IF age >= 0 AND age <= 12 THEN
        DISPLAY "You are a Child."
    ELSE IF age >= 13 AND age <= 19 THEN
        DISPLAY "You are a Teenager."
    ELSE IF age >= 20 AND age <= 64 THEN
        DISPLAY "You are an Adult."
    ELSE IF age >= 65 THEN
        DISPLAY "You are a Senior."
    ELSE
        DISPLAY "Invalid age entered."
    ENDIF
END




age = int(input("Enter the person's age: "))
if age <= 1:
    print("The person is an Infant.")
elif 1 < age < 13:
    print("The person is a Child.")
elif 13 <= age < 20:
    print("The person is a Teenager.")
else:
    print("The person is an Adult.")






weight = float(input("Enter the package weight in pounds: "))
if weight <= 2:
    cost_per_pound = 1.50
elif weight <= 6:
    cost_per_pound = 3.00
elif weight <= 10:
    cost_per_pound = 4.00
else:
    cost_per_pound = 4.75
total_cost = weight * cost_per_pound
print(f"Shipping cost: ${total_cost:.2f}")


print("Menu:")
print("1. Hot Dog - $3.50")
print("2. Chili Dog - $4.50")
print("Toppings:")
print("Cheese - $0.50")
print("Peppers - $0.75")
print("Grilled Onions - $1.00")
hot_dog_type = int(input("Enter 1 for Hot Dog or 2 for Chili Dog: "))
if hot_dog_type == 1:
    base_price = 3.50
elif hot_dog_type == 2:
    base_price = 4.50
else:
    print("Invalid selection.")
    exit()
toppings_cost = 0.0
cheese = input("Would you like Cheese? (yes/no): ").strip().lower()
if cheese == "yes":
    toppings_cost += 0.50
peppers = input("Would you like Peppers? (yes/no): ").strip().lower()
if peppers == "yes":
    toppings_cost += 0.75
grilled_onions = input("Would you like Grilled Onions? (yes/no): ").strip().lower()
if grilled_onions == "yes":
    toppings_cost += 1.00
subtotal = base_price + toppings_cost
tax = subtotal * 0.07  # 7% tax
total = subtotal + tax
print("\nOrder Summary:")
print(f"Hot Dog Cost: ${base_price:.2f}")
print(f"Toppings Cost: ${toppings_cost:.2f}")
print(f"Tax (7%): ${tax:.2f}")
print(f"Total Cost: ${total:.2f}")