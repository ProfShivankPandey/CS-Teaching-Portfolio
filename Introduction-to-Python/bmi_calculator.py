"""
BMI Calculator
================

Calculates Body Mass Index (BMI) from user-provided height and weight,
then classifies the result into a standard BMI category.

Formula: BMI = weight (kg) / height (m) ** 2
"""


def calculate_bmi(weight_kg, height_m):
    """
    Calculate BMI using the standard formula.

    Uses the division operator (/) and exponentiation operator (**).
    """
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)


def classify_bmi(bmi):
    """
    Classify a BMI value into a standard weight category.

    Uses comparison operators (<, <=) to determine the correct range.
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi <= 24.9:
        return "Normal weight"
    elif bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("=== BMI Calculator ===")

    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters (e.g., 1.75): "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers.")
            return

        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        print(f"\nYour BMI is: {bmi}")
        print(f"Category: {category}")

    except ValueError:
        print("Invalid input. Please enter numeric values only.")


if __name__ == "__main__":
    main()
