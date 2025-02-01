def user_input():
    height = float(input("Enter your height in meters: "))
    weight = float(input("Enter your weight in kilograms: "))
    return height, weight

def calculateBmi(height, weight):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        decision = "Underweight"
    elif 18.5 <= bmi < 24.9:
        decision = "Normal weight"
    elif 25 <= bmi < 29.9:
        decision = "Overweight"
    else:
        decision = "Obesity"
    return bmi, decision

def displayResult(bmi, decision):
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Based on your BMI, you are classified as: {decision}")

def main():
    height, weight = user_input()
    bmi, decision = calculateBmi(height, weight)
    displayResult(bmi, decision)


main()