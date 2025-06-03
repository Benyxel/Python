grades = []

while True:
    try:
        user_input = input("Enter student grade (or type 'done' to finish): ")
        if user_input.lower() == "done":
            break
        grade = float(user_input)
        grades.append(grade)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if grades:
    total = 0
    for grade in grades:
        total += grade  
    average = total / len(grades)
    print(f"The average grade is: {average}")
else:
    print("No grades were entered.")


