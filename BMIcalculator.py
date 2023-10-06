def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    else:
        return "Overweight"
weight_kg = float(input("Enter your weight in kilograms: "))
height_m = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight_kg, height_m)
print(f"Your BMI is: {bmi:.2f}")

weight_status = interpret_bmi(bmi)
print(f"You are categorized as: {weight_status}")


