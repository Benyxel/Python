studentsMlist= []

def studentData():
    num_of_input = input("How many Students Do you wanna add? ")
    if not num_of_input.isdigit():
        print("You must enter a valid number to start the operation")
    else:   
        num_of_input = int(num_of_input)
        if num_of_input < 1:
            print("Number can't be less than '1'")
            

        for number in range(1, num_of_input + 1):
            total_course = []
            name = input(f"Enter Student {number} Name: ")
            program = input(f"Enter Student {number} Program: ")
            num_Course = int(input(f"Enter Number of courses for student {number}: "))
            for course_num in range(1, num_Course + 1):
                course = input(f"Course {course_num}: ")
                total_course.append(course)
            students = {
                'Name': name,
                'Program': program,
                'Course': num_Course,
                'AllCourses': total_course
            }
    studentsMlist.append(students)       
studentData() 
print(studentsMlist)
'''def unique_values():

    num_of_elements = input("How many elements do you want to add to the list? ")
    if not num_of_elements.isdigit():
        print("You must enter a valid number to start the operation")
    else:
                
        num_of_elements = int(num_of_elements)
        if num_of_elements < 1:
            print("Number can't be less than '1'")
            

        
        elements_list = []
        for i in range(num_of_elements):
            element = input(f"Enter element {i + 1}: ")
            elements_list.append(element)
        unique_values_set = set(elements_list)
        unique_values_list = list(unique_values_set)
        print("Unique values in the list are:", unique_values_list)
unique_values()

values = input("Enter value with space as ").strip().split()
non_unique=[]
unique=[]


conv_values = set(values)
for i in conv_values:
    counter = values.count(i)
    if  counter == 1:
        unique.append(i)
    else:
        non_unique.append(i)
print(f"unique: {unique}")
print(f"not unique: {non_unique}")'''