studentsMlist= []

def studentData():
    num_of_input = input("How many Students Do you wanna add? ")
    if not num_of_input.isdigit():
        print("You must enter a valid number to start the operation")
        return
    num_of_input = int(num_of_input)
    if num_of_input < 1:
        print("Number can't be less than '1'")
        return

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
    print(studentsMlist)
    
    

studentData() 

def unique_values():
    # Step 1: Take input for the number of elements
    num_of_elements = input("How many elements do you want to add to the list? ")
    if not num_of_elements.isdigit():
        print("You must enter a valid number to start the operation")
        return
    num_of_elements = int(num_of_elements)
    if num_of_elements < 1:
        print("Number can't be less than '1'")
        return

    # Step 2: Take input for each element and add it to the list
    elements_list = []
    for i in range(num_of_elements):
        element = input(f"Enter element {i + 1}: ")
        elements_list.append(element)

    # Step 3: Use a set to store unique values
    unique_values_set = set(elements_list)

    # Step 4: Convert the set back to a list if needed
    unique_values_list = list(unique_values_set)

    print("Unique values in the list are:", unique_values_list)

# Call the function to find unique values
unique_values()