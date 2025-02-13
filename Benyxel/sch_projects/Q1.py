
grades = (input("Enter your grade: "))
def check_grade(grades):
    
    for grade in grades:
        if grades >= "50":
            print("Pass")
        else:
            print("Fail")
            
check_grade(grades)


