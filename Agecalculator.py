current_year = int(input("Enter the current year: "))
current_month = int(input("Enter the current month (1-12): "))
current_day = int(input("Enter the current day (1-31): "))

birth_year = int(input("Enter your year of birth: "))
birth_month = int(input("Enter your month of birth (1-12): "))
birth_day = int(input("Enter your day of birth (1-31): "))

years = current_year - birth_year
months = current_month - birth_month
days = current_day - birth_day

if days < 0:
    months -= 1
    days += 31

if months < 0:
    years -= 1
    months += 12

print(f"Your age is {years} years, {months} months, and {days} days.")
