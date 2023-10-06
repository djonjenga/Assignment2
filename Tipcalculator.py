total_bill = float(input("Enter the total bill amount: "))
tip_option = int(input("Select a tip percentage (10, 12, or 15): "))
num_people = int(input("Enter the number of people splitting the bill: "))

if tip_option not in [10, 12, 15] or total_bill <= 0 or num_people <= 0:
    print("Invalid input. Please enter valid values.")
else:
    tip_percentage = tip_option
    amount_per_person = (total_bill * (1 + tip_percentage / 100)) / num_people
    print(f"Each person should pay: {amount_per_person:.2f}")
